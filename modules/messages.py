MESSAGES = {
    "init_tunnel": "Тунель инициализирован!\nId тунеля: <code>{}</code>",
    "bind": "Связь между чатами установлена!",
    "help":"/about - Расскажет, для чего нужен этот бот\n/init_tunnel - Инициализирует туннель и вернёт его id\n/bind [id туннеля]- связяжет чат с тредом",
    
    "about":"""
Здравствуйте! Этот бот нужен для безопасного взаимодействия между основной командой и командой фрилансеров!

Допустим, у вас есть основная команда разработчиков и есть люди со стороны, которые помогают в разработке
только одного определённого продукта. 

Для удобства организации разработки нескольких проектов вы решили создать топик (по простому <code>тема</code> или <code>группа чатов</code>) и разделить его на несколько тредов. 
Фрилансеров вы не сможете добавить в топик, не \"спалив\" диалоги в командах разработки других продуктов, так уж устроен телеграм...

Но решение есть — бот-связист! Все сообщения треда будут пересылаться в чат фрилансеров и наоборот!
И вуаля! Безопасная связь установлена! Фриалансеры теперь не видят сообщения других команд!

PS
Вы можете создать неограниченное количество туннелей
""",

    "how it to use":"""
- Вам необходимо сперва добавить бота в топик, потом добавить в чат фрилансеров, выдав ему права администратора

- После этого войдите в нужный тред и введите команду /init_tunnel. Она вернёт вам id тунеля. Нажав на текст появившегося сообщения, вы его скопируете

- Дальше отправьте одному из фрилансеров id личным сообщением в телеграм, whatsapp или хоть голубиной почтой

- После этого кто-либо из чата фрилансеров должен ввести команду /bind [полученный id]  (без квадратных скобок, не бойтесь :) )

- Наслаждайтесь безопасным деловым общением :)"""
}