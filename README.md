# Курсовая работа по управлению проектами

### Инструкция по рабочему процессу для contributors

### 1. Скачиваем себе репозиторий в первый раз
* Заходим в [наш репозиторий](https://github.com/ovsyannikovas/coworking_website)
* Нажимаем **Code** и копируем ссылку
* Открываем консоль в папке, где хотите, чтобы находилась папка с репозиторием
* `git clone скопированная_ссылка`

### 2. Загружаем последнюю версию репозитория к себе на ветку
* Переходим в папку скачанного репозитория
* Открываем консоль
* `git checkout ваша_ветка`
* `git pull --no-commit origin main`

### 3. Загружаем изменения на свою ветку
Перед выполнением пункта убедитесь, что на вашей ветке последняя версия репозитория (пункт 2)!
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
* Нажимаем **Create pull request**
* Содержательно заполняем форму согласно шаблону (в поле title, где, скорее всего, стоит имя вашей ветки, продублируйте "Что изменилось (кратко)?")
