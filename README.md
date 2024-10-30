# 1 - калькулятор
создать образ: docker build -t calc .  
запустить образ: docker run calc  
Примеры запуска и команд ниже  
![image](https://github.com/user-attachments/assets/9e5b4330-ee0c-48da-9def-5c8c73be06e6)
![image](https://github.com/user-attachments/assets/d6ec1648-d1ff-4d67-b77f-4b637bf7a7c8)
# 2, 3 - создание пайплайна и внедрение инструментов безопасности
Делали в GitLab  
4 этапа:
![image](https://github.com/user-attachments/assets/8a3fbffc-2e23-46d5-8408-27e6296df7a5)
1) сканирование semgrep
2) сборка образа
3) сканирование trivy
4) развёртывание и проверка
# 4 - отчёты инструментов безопасности
semgrep:  
никаких уязвимостей  
![image](https://github.com/user-attachments/assets/6288b52b-a4da-410e-9267-ec8eb21bd6df)
trivy:  
![image](https://github.com/user-attachments/assets/5aab5ddd-5fcc-4e2d-9a7c-8b7c3399e5cb)
уязвимость debian пакета, критичность - низкая  
большинство уязвимотсей можно устранить обновлением пакетов (либо самой ОС, либо питона)  
на скрине ниже показана уязвимость связанная с питоном, а именно надо обносить вермсию pip
![image](https://github.com/user-attachments/assets/928b403b-04bb-43dd-a236-2ad2b639dd82)
