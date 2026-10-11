# Prey для ОС Аврора

[English](README.md) | Русский

Порт Prey (2006) на ОС Аврора.

Prey - шутер от первого лица, разработанный студией Human Head Studios
и изданный 2K Games в 2006 году на движке id Tech 4. В 2011 году
id Software открыла исходный код движка id Tech 4 (GPL). Этот порт основан на
проекте [idTech4A++ (Quake4Doom)](https://github.com/glKarin/com.n0n3m4.diii4a)
от glKarin - форке движка id Tech 4 с рендером на OpenGL ES и поддержкой
мобильных платформ.

## Автор порта
Порт сделан разработчиком [sashikknox](https://boosty.to/sashikknox).
Новости о новых портах игр на ОС Аврора (на русском языке) публикуются
в Telegram-канале: https://t.me/auroraosgames — подписывайтесь!

## Дисклеймер

В пакете содержится только **движок** игры (открытый исходный код,
GPL). Игровые данные (уровни, модели, текстуры, звуки, pk4-файлы
из `base`) в пакет **не входят** - они по-прежнему защищены авторским
правом правообладателей. Для игры нужна легально приобретённая
копия Prey.

При первом запуске встроенный лаунчер попросит указать папку
с легально приобретёнными игровыми данными (в ней должен быть
каталог `base` с pk4-файлами); выбранный путь сохраняется между
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


## Сборка

Проект собирается через CMake, основной проект лежит в `prey/doom3/neo`.
Пример конфигурации для ОС Аврора:

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

Подробное описание флагов сборки смотрите в [prey/README.md](prey/README.md).

## Лицензия

Исходный код движка распространяется под лицензией **GNU GPL v3**
(см. файл `LICENSE` в каталоге `prey`). Игровые данные Prey
не покрываются этой лицензией и остаются собственностью
правообладателей.

## Лицензии сторонних библиотек

В исходниках проекта поставляются сторонние библиотеки, каждая под
своей лицензией (тексты лицензий лежат в каталогах соответствующих
библиотек):

| Библиотека | Каталог | Лицензия |
| ---------- | ------- | -------- |
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
