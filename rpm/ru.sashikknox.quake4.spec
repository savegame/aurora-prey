%define _app_orgname ru.sashikknox
%define _app_appname quake4
%define _app_launcher_name Quake 4

Name:       %{_app_orgname}.%{_app_appname}
Summary:    Quake 4 for Aurora OS
Release:    1
Version:    1.0.0
Group:      Amusements/Games
License:    GPLv3
Source0:    %{name}.tar.gz

# SDL2 is built from the fork inside this package and installed next to the
# binary, so the system must not look for it as an external dependency
%define __requires_exclude ^libSDL2.*\\.so.*$
%define __provides_exclude_from ^%{_datadir}/%{name}/lib/.*\\.so.*$

BuildRequires: rsync
BuildRequires: patchelf
BuildRequires: ninja
BuildRequires: cmake
BuildRequires: extra-cmake-modules

# SDL2 fork with the Aurora OS fixes, built from the libsdl submodule
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(libpulse)

# engine dependencies taken from the Aurora OS repository
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(vorbisfile)

%description
Quake 4 port to Aurora OS, built on the idTech4A++ branch of idTech4.
The game resources are not distributed with the package: point the launcher
at a legally installed copy of the game.

%prep
%setup -q -n %{name}-%{version}

%build
# The SDL2 fork carries the Aurora OS fixes and is what the game runs against.
# It is not what the engine is compiled against, though: the fork is binary
# compatible with the SDL2 in the repository and declares the same headers, so
# the engine links the system one at build time and finds the fork at runtime
# through the rpath, where it sits inside the package under the same soname.
# The direction is the safe one — the fork (2.30) is newer than the system
# library (2.24), so every symbol the older headers declare is there.
cmake \
    -G Ninja \
    -DCMAKE_MAKE_PROGRAM=/usr/bin/ninja \
    -Bbuild/%{_arch}/libsdl \
    -DCMAKE_BUILD_TYPE=Release \
    -DSDL_PULSEAUDIO=ON \
    -DSDL_RPATH=OFF \
    -DSDL_AUDIO=ON \
    -DSDL_STATIC=OFF \
    -DSDL_WAYLAND=ON \
    -DSDL_X11=OFF \
    -DSDL_WAYLAND_LIBDECOR=OFF \
    libsdl

cmake --build build/%{_arch}/libsdl -j`nproc`
pushd build/%{_arch}/libsdl
rsync -avP include-config-release/SDL2/* include/SDL2/
rsync -avP *.so* lib/
popd

# the engine: Quake 4 only, GLES3, with the port turned on
cmake \
    -G Ninja \
    -DCMAKE_MAKE_PROGRAM=/usr/bin/ninja \
    -Bbuild/%{_arch}/quake4es \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_D3=OFF \
    -DBUILD_PREY=OFF \
    -DBUILD_ETQW=OFF \
    -DBUILD_D3_MOD=OFF \
    -DBUILD_Q4_MOD=OFF \
    -DBUILD_Q4=ON \
    -DOPENGLES3=ON \
    -DAURORA=ON \
    -DAURORA_FBO=ON \
    -DAURORA_LAUNCHER=ON \
    -DAURORA_ORG=%{_app_orgname} \
    -DAURORA_APP=%{_app_appname} \
    -DUSE_SYSTEM_OGGVORBIS=ON \
    -DUSE_SYSTEM_CURL=ON \
    -DCURL_LIBRARY=%{_libdir}/libcurl.so \
    -DUSE_SYSTEM_FREETYPE=OFF \
    -S quake4es \
    -B build/%{_arch}/quake4es

cmake --build build/%{_arch}/quake4es -j`nproc`

%install
# the engine binary and the game library
install -m 755 -D build/%{_arch}/quake4es/doom3/neo/Quake4 %{buildroot}%{_bindir}/%{name}
install -m 755 -D build/%{_arch}/quake4es/doom3/neo/libq4game.so -t %{buildroot}%{_datadir}/%{name}/lib

# SDL2 from the fork travels inside the package and wins at runtime over the
# system one, because the binary's rpath points here
install -D -s build/%{_arch}/libsdl/libSDL2-2.0.so* -t %{buildroot}%{_datadir}/%{name}/lib

# SDL knows only a handful of game controllers by itself, the community mapping
# database from the SDL_GameControllerDB submodule teaches it hundreds more. The
# engine reads it from the package directory; it is installed here rather than
# with the engine's GAMECONTROLLERDB_FILE, which only copies it into the build
# tree. Users can add their own mappings in gamecontrollerdb.txt in the save
# directory, it is read after this one and wins
install -m 644 -D SDL_GameControllerDB/gamecontrollerdb.txt %{buildroot}%{_datadir}/%{name}/gamecontrollerdb.txt

# default bindings for the game controller keys; the engine applies them at
# startup to the keys the user's configs leave unbound
install -m 644 -D gamepad.cfg %{buildroot}%{_datadir}/%{name}/gamepad.cfg

# then patch elf path for game binary
patchelf --force-rpath --set-rpath %{_datadir}/%{name}/lib %{buildroot}%{_bindir}/%{name}
# install icons files
install -m 655 -D icons/86.png  %{buildroot}%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
install -m 655 -D icons/108.png %{buildroot}%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
install -m 655 -D icons/128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -m 655 -D icons/172.png %{buildroot}%{_datadir}/icons/hicolor/172x172/apps/%{name}.png

sed "s/__ORGNAME__/%{_app_orgname}/g" game.desktop.in>%{name}.desktop
sed -i "s/__APPNAME__/%{_app_appname}/g" %{name}.desktop
sed -i "s/__X_APPLICATION__/%{firejail_section}/g" %{name}.desktop
sed -i "s/__LAUNCHER_NAME__/%{_app_launcher_name}/g" %{name}.desktop

install -m 655 -D %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/172x172/apps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
