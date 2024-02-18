buttons = document.getElementsByClassName("but")
console.log(buttons)
Array.from(buttons).forEach(el =>{
    el.addEventListener('click', click)
})

// Определяем функцию которая принимает в качестве параметров url и данные которые необходимо обработать:
const postData = async (url = '', data = {}) => {
    // Формируем запрос
    const response = await fetch(url, {
      // Метод, если не указывать, будет использоваться GET
      method: 'POST',
     // Заголовок запроса
      headers: {
        'Content-Type': 'application/json'
      },
      // Данные
      body: JSON.stringify(data)
    });
    return response.json(); 
  }


function click(){
    task = document.getElementById(this.id.split('_')[0])
    task.className += ' disabled'
    task.setAttribute('aria-disabled', 'true')
    this.setAttribute('disabled', 'true')
    div_alert = document.createElement('div');
    div_alert.className = "alert alert-warning alert-dismissible d-flex align-items-center"
    div_alert.setAttribute('role', 'alert')

    
    div = document.createElement('div')
    div.textContent  = 'вы удалили задачу: ' + task.textContent
    
    btn = document.createElement('button')
    btn.className = 'btn-close'
    btn.setAttribute('data-bs-dismiss', 'alert')
    btn.setAttribute('type', 'button')
    btn.setAttribute('aria-label', 'Close')
    
    
    div_alert.append(div)
    div_alert.append(btn)
    place = document.getElementById('main')
    place.append(div_alert)
    data = {text: task.textContent}
    postData('/delete', data)
    
}