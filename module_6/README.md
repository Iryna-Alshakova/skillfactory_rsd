
# Car Price Prediction
### Задача: построить модель, которая предсказывает стоимость автомобиля по его характеристикам

Была предоставлена таблица с различными характеристиками автомобилей без цен. Их нужно было предсказать с помощью созданной модели.
Точность модели проверялась метрикой MAPE.  

Для построения модели были собраны данные об автомобилях c сайта auto.ru. Собирались данные автомобилей только тех марок, которые присутствовали в предоставленном датасете. 

Собранные данные были очищены. Были сгенерированы дополнительные признаки.

При поиске предсказательной модели были использованы модели sklearn, которые были определены, как наиболее оптимальные с помощью Lazy Predict, а также CatBoostRegressor.

### Содержание
[Парсинг](https://github.com/Iryna-Alshakova/skillfactory_rsd/blob/main/module_6/Data%20Parsing.ipynb)    
[Обработка полученных данных](https://github.com/Iryna-Alshakova/skillfactory_rsd/blob/main/module_6/Car%20price%20data.ipynb)  
[Выбор моделей sklearn](https://github.com/Iryna-Alshakova/skillfactory_rsd/blob/main/module_6/LazzyPredict.ipynb)  
[Предсказательная модель](https://github.com/Iryna-Alshakova/skillfactory_rsd/blob/main/module_6/Prediction%20model.ipynb)
