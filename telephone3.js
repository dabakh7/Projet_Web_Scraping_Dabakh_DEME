const pg = require('pg')

var config = {
    user: 'postgres', // env var: PGUSER
    database: 'BD_Scraping', // env var: PGDATABASE
    password: 'test123', // env var: PGPASSWORD
    host: 'localhost', // Server hosting the postgres database
    // port: 35432, // env var: PGPORT
    max: 20, // max number of clients in the pool
    idleTimeoutMillis: 30000 // how long a client is allowed to remain idle before being closed
}


const pool = new pg.Pool(config)

const puppeteer = require('puppeteer')

async function getData(){
    const browser = await puppeteer.launch({headless:true})
    const page = await browser.newPage()
    await page.goto('https://www.boulanger.com/c/iphone')

    let products = await page.evaluate(function(){
        let data = new Array()

        const div = document.querySelector(".row.product-list__items")

        const elements = div.querySelectorAll(".row.product-item__row")

        elements.forEach(element =>{
            let item_data = {}

            // item_data.image = element.querySelector("img.product-item__image").getAttribute('src')
            item_data.marque = element.querySelector('h2.product-item__label').innerText
            item_data.prix = element.querySelector('p.price__amount').innerText.replace('€','').replace(' ',',').split(',')[0]
            item_data.prix = (+item_data.prix) * 650
            
        
            data.push(item_data)
        })
        return data
    })
    console.log(products)
    // browser.close()

    for(donne of products){
       const entrer = "INSERT INTO Telephone3(marque, prix) values ($1,$2)"
       const datas = [donne.marque, donne.prix]
    //    pool.query(entrer,datas)
    }
    pool.end()
}   
getData()

