<h3> <a href="https://github.com/GFyuliya/Portfolio/tree/main/Hexlet%20project%20QA-engineer">Hexlet project QA-engineer</a></h3>
<h4>В этом проекте проведено тестирование небольшого <a href="https://hexlet-products-store.vercel.app/"> интернет-магазина</a></h4>
<h6>Учебный проект с курса <a href="https://ru.hexlet.io/programs/qa-engineer"> "Инженер по тестированию"</a> от Хекслет</h6>
<h6>По требованию курса был использован язык разметки YAML для оформления тест-кейсов, баг-репортов и других документов.</h6>
<h4>Для разработки интернет-магазина разработчику дали следующее задание</h4>
<ul>
  <li>Нужно разработать интерфейс интернет-магазина с просмотром и фильтрацией товаров, а также добавлением их в корзину.</li>
  <li>Ключевой возможностью магазина будет адаптивная верстка, чтобы он был удобным на мобильных устройствах. Также магазин будет SPA-приложение, которое не перезагружает страницу. Пользователь будет просматривать каталог товаров, фильтруя их и пользуясь постраничным выводом.</li>
  <li>На странице товара и в каталоге нужно выводить название, рейтинг, цена со скидкой и без нее. Пользователь будет добавлять товар в корзину и продолжать выбирать товары в каталоге.</li>
  <li>На странице корзины пользователь cможет удалить товар из корзины, продолжить выбирать товары в каталоге, оформить заказ с переходом на страницу оплаты. Корзина будет хранится в сессии браузера.</li>
</ul>

<h4>Задачи</h4>
<ol>
  <li>Составить список требований</li>
  <li>Провести тест-анализ и составить тест-кейсы</li>
  <li>Провести тестирование по ранее созданным тест-кейсам, указать статус тест-кейсов (pass/fail)</li>
  <li>Подготовить баг-репорты</li>
  <li>Выполнить регрессионное тестирование <a href="https://products-store-git-v2bugfixes-hexlet-components.vercel.app/">новой версии магазина</a> и подготовить отчет о пройденных тест-кейсах и новых баг-репортах</li>
</ol>


<h3> <a href="https://github.com/GFyuliya/Portfolio/tree/main/Тестирование%20Регистрации">Тестирование Регистрации</a></h3>
<h4>В этом проекте проведено тестирование <a href="https://www.knitshop.ru/auth/registration/"> регистрации онлайн-магазина Knitshop.ru</a></h4>
<h4>Тест-кейсы были созданы в TestRail</h4>
<h4>Требования для формы регистрации (для более интересного процесса я добавила требования, отмечены *): </h4>
<ol>
  <li> Форма содержит поля: "Фамилия Имя Отчество", "E-mail", "Телефон", "Пароль", "Подтверждение пароля", "Введите код" </li>
  <li> Все поля обязательны к заполнению</li>
  <li> Автоматическая валидация без отправки формы для всех полей </li>
  <li> * Для поля "Фамилия Имя Отчество" разрешается ввод на кириллице и латинице, от 2 до 60 символов (только буквы, пробелы и тире)</li>
  <li> * Для поля "E-mail" есть подсказка в поле, формат: example@example.com</li>
  <li> * На один номер телефона можно зарегистрировать только одного пользователя</li>
  <li> На один e-mail можно зарегистрировать только одного пользователя</li>
  <li> * Для поля "Введите код" установлено ограничение на длину ввода - 5 символов</li>
  <li> * Для подтверждения регистрации отправляется письмо на указанный e-mail с верификационной ссылкой</li>
</ol>
