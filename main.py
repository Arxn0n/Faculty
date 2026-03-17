from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

@app.get(
        "/GetEmployeers",
        tags=["Получение данных из БД"],
        summary= "Получение всех сотрудников",
        )
def get_bd_employeers():
    return "Таблица сотрудников"

@app.post(
        "/AddEmplayeer",
        tags=["Добавление данных"],
        summary= "Добавление сотрудника",
        )
def add_enplayeer():
    return "Сотрудник добавлен"
    
@app.get(
        "/GetAchivments",
        tags=["Получение данных из БД"],
        summary= "Получение достижений",
        )
def get_bd_achivments():
    return "Таблица достижений"

@app.post(
        "/AddAcivment",
        tags=["Добавление данных"],
        summary= "Добавление достижения",
        )
def add_enplayeer():
    return "Достежение добавлено"

@app.get(
        "/GetPublications",
        tags=["Получение данных из БД"],
        summary= "Получение публикаций",
        )
def get_bd_publications():
    return "Таблица публикаций"

@app.post(
        "/AddPublication",
        tags=["Добавление данных"],
        summary= "Добавление публикации",
        )
def add_enplayeer():
    return "Публикация добавлена"

@app.get(
    "/GetReportEmployeers",
    tags=["Работа с отчетами"],
    summary="Получение отчета по сотрудникам",
    )
def get_report():
    return "Получен отчет о сотрудниках"

@app.get(
    "/GetReportAcivments",
    tags=["Работа с отчетами"],
    summary="Получение отчета о достижениях",
    )
def get_report():
    return "Получен отчет о достижениях"

@app.get(
    "/GetReportPublication",
    tags=["Работа с отчетами"],
    summary="Получение отчета о публикациях",
    )
def get_report():
    return "Получен отчет о публикациях"

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)