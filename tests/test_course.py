import json

def test_get(app, client):
    res = client.get('/course')
    assert res.status_code == 200
    expected = {{
                "data": [
                    {
                    "date_created": "2019-12-25 12:57:58", 
                    "date_updated": "2020-12-18 16:18:29", 
                    "description": "Scala is a multi-paradigm, general-purpose programming language.", 
                    "id": 1, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 20.0, 
                    "title": "The Art of Scala"
                    }, 
                    {
                    "date_created": "2019-03-16 05:15:39", 
                    "date_updated": "2020-12-29 08:40:44", 
                    "description": "Agile practices discover requirements and develop solutions through collaborative effort.", 
                    "id": 2, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 30.0, 
                    "title": "The Joy of Agile"
                    }, 
                    {
                    "date_created": "2020-09-13 14:40:39", 
                    "date_updated": "2020-09-23 10:52:39", 
                    "description": "Pages is a word processor developed by Apple Inc.", 
                    "id": 3, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 50.0, 
                    "title": "Talks About Pages"
                    }, 
                    {
                    "date_created": "2020-07-20 17:51:23", 
                    "date_updated": "2020-08-04 12:06:58", 
                    "description": "Microsoft Visual Studio is an integrated development environment (IDE) from Microsoft.", 
                    "id": 4, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 20.0, 
                    "title": "This Is A Course About Visual Studio"
                    }, 
                    {
                    "date_created": "2020-07-04 01:02:49", 
                    "date_updated": "2021-01-31 15:07:20", 
                    "description": "Scala is a multi-paradigm, general-purpose programming language.", 
                    "id": 5, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 30.0, 
                    "title": "Even A Kid Can Learn Scala!"
                    }, 
                    {
                    "date_created": "2018-11-01 18:54:31", 
                    "date_updated": "2020-05-19 08:24:37", 
                    "description": "Amazon Aurora is a relational database service developed and offered by AWS.", 
                    "id": 6, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 10.0, 
                    "title": "A Simple Approach to Aurora"
                    }, 
                    {
                    "date_created": "2020-08-23 06:31:30", 
                    "date_updated": "2021-02-09 01:22:38", 
                    "description": "Amazon Web Services (AWS) is an on-demand cloud computing platform, and a subsidiary of Amazon.", 
                    "id": 7, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 40.0, 
                    "title": "AWS: The Complete Blueprint"
                    }, 
                    {
                    "date_created": "2018-02-05 06:12:43", 
                    "date_updated": "2020-01-15 10:14:05", 
                    "description": "Microsoft Visual Studio is an integrated development environment (IDE) from Microsoft.", 
                    "id": 8, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 20.0, 
                    "title": "Do not Visual Studio Without This Course"
                    }, 
                    {
                    "date_created": "2020-11-04 00:45:40", 
                    "date_updated": "2020-11-26 12:00:56", 
                    "description": "Keynote is a presentation program developed by Apple Inc.", 
                    "id": 9, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 20.0, 
                    "title": "Essential KeyNote"
                    }, 
                    {
                    "date_created": "2018-03-23 11:46:56", 
                    "date_updated": "2018-07-26 16:24:09", 
                    "description": "Keynote is a presentation program developed by Apple Inc.", 
                    "id": 10, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 50.0, 
                    "title": "Beginners Guide To KeyNote"
                    }
                ]
                }}
    assert expected = json.loads(res.get-data(as_text=True))
    res = client.get('/course?page-number=1&page-size=10&title-words=z')
    assert res.status_code == 200
    expected = {{
                "data": [
                    {
                    "date_created": "2019-07-26 05:15:10", 
                    "date_updated": "2019-08-01 17:45:58", 
                    "description": "Azure is a cloud-based computing platform created by Microsoft.", 
                    "id": 62, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 40.0, 
                    "title": "Super Azure"
                    }, 
                    {
                    "date_created": "2020-02-07 10:13:22", 
                    "date_updated": "2020-09-20 22:48:14", 
                    "description": "Azure is a cloud-based computing platform created by Microsoft.", 
                    "id": 77, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 20.0, 
                    "title": "Cracking the Secrets of Azure"
                    }, 
                    {
                    "date_created": "2018-03-14 08:39:43", 
                    "date_updated": "2019-02-27 15:54:33", 
                    "description": "Azure is a cloud-based computing platform created by Microsoft.", 
                    "id": 113, 
                    "image_path": "", 
                    "on_discount": true, 
                    "price": 20.0, 
                    "title": "Expert Azure"
                    }
                ]
                }}
    assert expected = json.loads(res.get-data(as_text=True))
    res = client.get('/course?page-number=2&page-size=2&title-words=z,x')
    assert res.status_code == 200
    expected = {{
                "data": [
                    {
                    "date_created": "2019-11-28 22:03:49", 
                    "date_updated": "2020-04-01 00:36:41", 
                    "description": "Microsoft PowerPoint is a presentation program.", 
                    "id": 44, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 30.0, 
                    "title": "My Microsoft PowerPoint Experience Taught Me These Rules"
                    }, 
                    {
                    "date_created": "2020-05-15 08:18:33", 
                    "date_updated": "2020-12-22 03:59:41", 
                    "description": "Microsoft PowerPoint is a presentation program.", 
                    "id": 46, 
                    "image_path": "", 
                    "on_discount": false, 
                    "price": 20.0, 
                    "title": "Expert Microsoft PowerPoint"
                    }
                ]
                }}
    assert expected = json.loads(res.get-data(as_text=True))

