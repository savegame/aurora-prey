# Prey for Aurora OS

English | [Русский](README.ru.md)

A Prey (2006) port for Aurora OS.

Prey is a first-person shooter developed by Human Head Studios and
published by 2K Games in 2006, built on the id Tech 4 engine. In 2011
id Software released the id Tech 4 engine source code under the GPL.
This port is based on the
[idTech4A++ (Quake4Doom)](https://github.com/glKarin/com.n0n3m4.diii4a)
project by glKarin - an id Tech 4 fork with an OpenGL ES renderer and
support for mobile platforms.

## Port author
The port was made by the developer [sashikknox](https://boosty.to/sashikknox).
News about new game ports for Aurora OS (in Russian) is published
in the Telegram channel: https://t.me/auroraosgames — subscribe!

## Disclaimer

The package contains only the game **engine** (open source code,
GPL). Game data (levels, models, textures, sounds, pk4 files from
`base`) is **not included** - it remains copyrighted by its
rights holders. To play you need a legally purchased copy of Prey.

On first launch the built-in launcher will ask you to point to the
folder with your legally obtained game data (it must contain the
`base` directory with pk4 files); the selected path is saved between
launches.

## Screenshots 
|<img width="2400" height="1080" alt="Снимок_Экрана_20261020_012" src="https://github.com/user-attachments/assets/23f8fd94-1360-4c5c-a94f-402d17576899" />|<img width="2400" height="1080" alt="Снимок_Экрана_20261020_011" src="https://github.com/user-attachments/assets/206a796e-f145-4668-aae6-d9a28b88cfb5" />|
|:-:|:-:|
|<img width="2400" height="1080" alt="Снимок_Экрана_20261020_003" src="https://github.com/user-attachments/assets/ad2ef3b8-e2cb-49d7-b7fb-ac11dcef559b" />|<img width="2400" height="1080" alt="Снимок_Экрана_20261020_001" src="https://github.com/user-attachments/assets/77b806c4-88c9-45e0-940c-9668f5e8414b" />|

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


## Building

The project is built with CMake, the main project lives in
`prey/doom3/neo`. Example configuration for Aurora OS:

```sh
cmake ../prey/doom3/neo \
    -DCMAKE_BUILD_TYPE=Release \
    -DAURORA=ON \
    -DAURORA_FBO=ON \
    -DAURORA_LAUNCHER=ON \
    -DAURORA_ORG=ru.sashikknox \
    -DAURORA_APP=prey \
    -DBUILD_D3=OFF \
    -DBUILD_Q4=OFF \
    -DBUILD_ETQW=OFF
make -j$(nproc)
```

See [prey/README.md](prey/README.md) for a detailed description
of the build flags.

## License

The engine source code is distributed under the **GNU GPL v3**
license (see the `LICENSE` file in the `prey` directory).
Prey game data is not covered by this license and remains the
property of its rights holders.

## Third-party library licenses

Third-party libraries bundled with the project sources, each under
its own license (license texts live in the corresponding library
directories):

| Library | Directory | License |
| ------- | --------- | ------- |
| SDL2 | `libsdl/` | zlib |
| SDL_GameControllerDB | `SDL_GameControllerDB/` | zlib |
| Dear ImGui | `prey/doom3/neo/externlibs/imgui/` | MIT |
| OpenAL Soft | `prey/doom3/neo/externlibs/openal-soft/` | LGPL v2.1+ |
| libcurl | `prey/doom3/neo/externlibs/curl/` | curl (MIT/X style) |
| FreeType | `prey/doom3/neo/externlibs/freetype/` | FreeType License (FTL) / GPLv2 |
| libjpeg | `prey/doom3/neo/externlibs/jpeg-8d/` | IJG (BSD-like) |
| libogg, libvorbis | `prey/doom3/neo/externlibs/libogg/`, `.../libvorbis/` | BSD 3-Clause |
| miniz, minizip | `prey/doom3/neo/externlibs/miniz/`, `.../minizip/` | MIT / zlib |
| minimp3 | `prey/doom3/neo/externlibs/minimp3/` | CC0 (public domain) |
| stb | `prey/doom3/neo/externlibs/stb/` | public domain / MIT (dual) |
| SOIL | `prey/doom3/neo/externlibs/soil/` | public domain |
| TinyEXR | `prey/doom3/neo/externlibs/tinyexr/` | BSD |
| sse2neon | `prey/doom3/neo/externlibs/sse2neon/` | MIT |
| irrXML | `prey/doom3/neo/externlibs/irrxml/` | zlib |
