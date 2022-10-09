# Курсовая работа по управлению проектами

### Инструкция по рабочему процессу для collaborators

### 1. Скачиваем себе репозиторий в первый раз
* Заходим в [наш репозиторий](https://github.com/ovsyannikovas/coworking_website)
* Нажимаем **Code** и копируем ссылку
* Открываем консоль в папке, где хотите, чтобы находилась папка с репозиторием
* `git clone скопированная_ссылка`

### 2. Загружаем последнюю версию репозитория в последующие разы
* Заходим в [наш репозиторий](https://github.com/ovsyannikovas/coworking_website)
* Нажимаем **Code** и копируем ссылку
* Переходим в папку скачанного репозитория
* Открываем консоль
* `git pull скопированная_ссылка`

### 3. Загружаем изменения на свою ветку
* Переходим в папку скачанного репозитория
* Открываем консоль
* `git checkout ваша_ветка`
* `git add *`
* Проверяем командой `git status`, что добавились только нужные файлы
* `git commit -m "что_добавлено"`
* `git push origin ваша_ветка`

### 4. Загружаем изменения из своей ветки в `main`
* Заходим в [наш репозиторий](https://github.com/ovsyannikovas/coworking_website)
* Заходим в **Pull requests**
* Нажимаем **New pull request**
* Выбираем **base:main -> compare:ваша_ветка**
* ...
