# Quake 4 для ОС Аврора

Порт Quake 4 на ОС Аврора.

Quake 4 - шутер от первого лица, разработанный студией Raven Software
и изданный id Software в 2005 году на движке id Tech 4. В 2011 году
id Software открыла исходный код движка id Tech 4 (GPL), а игровой код
Quake 4 был выпущен под GPL в составе Quake 4 SDK. Этот порт основан на
проекте [idTech4A++ (Quake4Doom)](https://github.com/glKarin/com.n0n3m4.diii4a)
от glKarin - форке движка id Tech 4 с рендером на OpenGL ES и поддержкой
мобильных платформ.

## Автор порта

Я (sashikknox) портировал эту и многие другие игры для ОС Аврора.
Так же я пишу про новые порты игр на ОС Аврора (на русском) в своём
канале: https://t.me/auroraosgames Подписывайтесь!

## Дисклеймер

В пакете содержится только **движок** игры (открытый исходный код,
GPL). Игровые данные (уровни, модели, текстуры, звуки, pk4-файлы
из `q4base`) в пакет **не входят** - они по-прежнему защищены авторским
правом id Software / Bethesda. Для игры нужна легально приобретённая
копия Quake 4. Купить можно в Steam:
https://store.steampowered.com/app/2210/Quake_IV/

При первом запуске встроенный лаунчер попросит указать папку
с легально приобретёнными игровыми данными (в ней должен быть
каталог `q4base` с pk4-файлами); выбранный путь сохраняется между
запусками.

## Особенности порта

- Рендер на OpenGL ES 2/3: игра работает на мобильных GPU без
  полноценного desktop OpenGL.
- Рендер через промежуточный FBO: кадр рисуется в offscreen
  framebuffer и выводится на экран одним квадом. Это даёт корректный
  поворот и масштабирование картинки под ориентацию экрана устройства,
  а так же настройку разрешения 3D-рендера для повышения
  производительности.
- Встроенный in-process лаунчер на Dear ImGui: выбор папки с игровыми
  ресурсами и базовые настройки до старта движка.
- Тач-интерфейс: виртуальный стик движения, область осмотра и кнопки
  действий с поддержкой мультитача - в игру можно играть полностью
  без клавиатуры, мыши и геймпада.
- Поддержка геймпадов через SDL_GameController API: встроенная база
  маппингов сообщества (SDL_GameControllerDB), привязки кнопок
  по умолчанию, определение подключения и отключения "на лету".
- Поддержка внешних клавиатуры и мыши.
- Интеграция с ОС Аврора: сборка под aarch64, armv7hl, x86_64, упаковка в RPM,
  иконки и desktop-файл, корректная работа с ориентацией экрана.
- Звук через OpenAL Soft.

## Скриншоты

|<img width="600" height="320" alt="Снимок_Экрана_20260911_008" src="https://github.com/user-attachments/assets/0e4e630e-93e0-4512-b8e0-7a144b4ae873" />|<img width="600" height="320" alt="Снимок_Экрана_20260911_007" src="https://github.com/user-attachments/assets/8e10199b-3030-4712-95a2-790345b60158" />|
|:-:|:-:|
|<img width="600" height="320" alt="Снимок_Экрана_20260911_005" src="https://github.com/user-attachments/assets/3f698be3-e9a1-4a54-a291-0eab8acd4628" />|<img width="600" height="320" alt="Снимок_Экрана_20260911_003" src="https://github.com/user-attachments/assets/ba73c9cf-3606-4bca-b697-a837bd266a12" />|

## Сборка

Проект собирается через CMake, основной проект лежит в `quake4es/doom3/neo`.
Пример конфигурации для ОС Аврора:

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

Подробное описание флагов сборки смотрите в [quake4es/README.md](quake4es/README.md).

## Лицензия

Исходный код движка распространяется под лицензией **GNU GPL v3**
(см. файл `LICENSE` в каталоге `quake4es`). Игровые данные Quake 4
не покрываются этой лицензией и остаются собственностью
id Software / Bethesda.

## Лицензии сторонних библиотек

В исходниках проекта поставляются сторонние библиотеки, каждая под
своей лицензией (тексты лицензий лежат в каталогах соответствующих
библиотек):

| Библиотека | Каталог | Лицензия |
| ---------- | ------- | -------- |
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
