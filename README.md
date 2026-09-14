# Quake 4 for Aurora OS

English | [Русский](README.ru.md)

A Quake 4 port for Aurora OS.

Quake 4 is a first-person shooter developed by Raven Software and
published by id Software in 2005, built on the id Tech 4 engine.
In 2011 id Software released the id Tech 4 engine source code under
the GPL, and the Quake 4 game code was released under the GPL as part
of the Quake 4 SDK. This port is based on the
[idTech4A++ (Quake4Doom)](https://github.com/glKarin/com.n0n3m4.diii4a)
project by glKarin - an id Tech 4 fork with an OpenGL ES renderer and
support for mobile platforms.

## Port author

I (sashikknox) ported this and many other games to Aurora OS.
I also write about new game ports for Aurora OS (in Russian) on my
channel: https://t.me/auroraosgames Subscribe!

## Disclaimer

The package contains only the game **engine** (open source code,
GPL). Game data (levels, models, textures, sounds, pk4 files from
`q4base`) is **not included** - it remains copyrighted by
id Software / Bethesda. To play you need a legally purchased copy of
Quake 4. You can buy it on Steam:
https://store.steampowered.com/app/2210/Quake_IV/

On first launch the built-in launcher will ask you to point to the
folder with your legally obtained game data (it must contain the
`q4base` directory with pk4 files); the selected path is saved between
launches.

## Port features

- OpenGL ES 2/3 renderer: the game runs on mobile GPUs without full
  desktop OpenGL.
- Rendering through an intermediate FBO: the frame is drawn into an
  offscreen framebuffer and presented as a single quad. This provides
  correct rotation and scaling for the device screen orientation, as
  well as adjustable 3D render resolution to improve performance.
- Built-in in-process launcher based on Dear ImGui: pick the game data
  folder and basic settings before the engine starts.
- Touch interface: virtual movement stick, look area and action buttons
  with multitouch support - the game is fully playable without a
  keyboard, mouse or gamepad.
- Gamepad support through the SDL_GameController API: bundled community
  mapping database (SDL_GameControllerDB), default button bindings,
  hotplug detection.
- External keyboard and mouse support.
- Aurora OS integration: builds for aarch64, armv7hl, x86_64, RPM
  packaging, icons and desktop file, correct screen orientation
  handling.
- Sound through OpenAL Soft.

## Screenshots

|<img width="600" height="320" alt="Снимок_Экрана_20260911_008" src="https://github.com/user-attachments/assets/0e4e630e-93e0-4512-b8e0-7a144b4ae873" />|<img width="600" height="320" alt="Снимок_Экрана_20260911_007" src="https://github.com/user-attachments/assets/8e10199b-3030-4712-95a2-790345b60158" />|
|:-:|:-:|
|<img width="600" height="320" alt="Снимок_Экрана_20260911_005" src="https://github.com/user-attachments/assets/3f698be3-e9a1-4a54-a291-0eab8acd4628" />|<img width="600" height="320" alt="Снимок_Экрана_20260911_003" src="https://github.com/user-attachments/assets/ba73c9cf-3606-4bca-b697-a837bd266a12" />|

## Building

The project is built with CMake, the main project lives in
`quake4es/doom3/neo`. Example configuration for Aurora OS:

```sh
cmake ../quake4es/doom3/neo \
    -DCMAKE_BUILD_TYPE=Release \
    -DAURORA=ON \
    -DAURORA_FBO=ON \
    -DAURORA_LAUNCHER=ON \
    -DAURORA_ORG=ru.sashikknox \
    -DAURORA_APP=quake4 \
    -DBUILD_D3=OFF \
    -DBUILD_PREY=OFF \
    -DBUILD_ETQW=OFF
make -j$(nproc)
```

See [quake4es/README.md](quake4es/README.md) for a detailed description
of the build flags.

## License

The engine source code is distributed under the **GNU GPL v3**
license (see the `LICENSE` file in the `quake4es` directory).
Quake 4 game data is not covered by this license and remains the
property of id Software / Bethesda.

## Third-party library licenses

Third-party libraries bundled with the project sources, each under
its own license (license texts live in the corresponding library
directories):

| Library | Directory | License |
| ------- | --------- | ------- |
| SDL2 | `libsdl/` | zlib |
| SDL_GameControllerDB | `SDL_GameControllerDB/` | zlib |
| Dear ImGui | `quake4es/doom3/neo/externlibs/imgui/` | MIT |
| OpenAL Soft | `quake4es/doom3/neo/externlibs/openal-soft/` | LGPL v2.1+ |
| libcurl | `quake4es/doom3/neo/externlibs/curl/` | curl (MIT/X style) |
| FreeType | `quake4es/doom3/neo/externlibs/freetype/` | FreeType License (FTL) / GPLv2 |
| libjpeg | `quake4es/doom3/neo/externlibs/jpeg-8d/` | IJG (BSD-like) |
| libogg, libvorbis | `quake4es/doom3/neo/externlibs/libogg/`, `.../libvorbis/` | BSD 3-Clause |
| miniz, minizip | `quake4es/doom3/neo/externlibs/miniz/`, `.../minizip/` | MIT / zlib |
| minimp3 | `quake4es/doom3/neo/externlibs/minimp3/` | CC0 (public domain) |
| stb | `quake4es/doom3/neo/externlibs/stb/` | public domain / MIT (dual) |
| SOIL | `quake4es/doom3/neo/externlibs/soil/` | public domain |
| TinyEXR | `quake4es/doom3/neo/externlibs/tinyexr/` | BSD |
| sse2neon | `quake4es/doom3/neo/externlibs/sse2neon/` | MIT |
| irrXML | `quake4es/doom3/neo/externlibs/irrxml/` | zlib |
