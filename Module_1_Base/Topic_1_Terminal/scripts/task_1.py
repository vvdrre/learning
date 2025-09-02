!#/bin/bash
echo "Введите имя"
read username
mkdir -p "$username"
echo "Привет, $username это товя перва папка" > "$username/welcome.txt"
echo "Папка '$username' и файл welcome.txt созданы"