but = document.querySelector('button')
but.addEventListener('click', click)

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
  text_ = document.getElementById('text').value
  data = {text: text_}
  postData('/create', data)
}