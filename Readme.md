# ASSIST MANAGER PRO 
An application to create, save, edit, update and/or delete projects used by project managers. Creates a database of users with there individual projects

### Technologies/Methods Used
- React
- CRUD
- API
- Render
- Django
- CSS
- POSTMAN
- SCHEMA
- Next 
- Tailwind

### WIREFRAMES

Component Architecture

<img src="https://i.imgur.com/yzRJlEt.png">
<img src="https://i.imgur.com/Ol6scgq.jpg">
<img src="https://i.imgur.com/T8tbZ5k.png">
<img src="https://i.imgur.com/IK10t6D.png">


### Routers

|Route | Element | Loader | Action | Summary |
|---------|-------------|----------|-----------|--------------|
| / | Index | indexLoader | | Display lists of projects with user name and title |
| /project/ :id | project| projectLoader | | Display the selected project|
| /project/create/ :id | | | projectCreateAction | creates a new project page with project information |
| /project/update/:id | | | projectUpdateAction | updates a pre-existing project with new/altered data |
| /project/delete/ :id | | | projectDeleteAction | deletes a previous project |
