Sure, here's the translated README for your project:

---

# ScrapyPriceMonitoring

This README provides a clear and detailed overview of the project, including the architecture, directory structure, installation and usage instructions, as well as specific modules for data extraction, transformation, and visualization.

A Python ETL for Price Monitoring

## A Python ETL for Price Monitoring

Python solution for pricing strategies. We have a pipeline and an ETL in Python that collects, consolidates, and generates insights about a specific category of products. The project will navigate to the website defined by you and extract data from dozens or hundreds of pages containing price information, titles, descriptions, and ratings. The data will be transformed using Pandas. A table will be assembled in a PostgreSQL database. Insights and dashboards will be generated automatically.

## Architecture

A Python ETL for Web Scraping

- Extraction - Scrapy
- Transformation and Load - Pandas
- Dashboard - Streamlit
- Database - PostgreSQL

### Diagram

![architecture](/pics/architecture.png)

### Excalidraw

[Excalidraw](https://link.excalidraw.com/l/8pvW6zbNUnD/4qYJqXpeRfP)

### Directory Structure

```plaintext
ScrapyPriceMonitoring/
├── scrapy_monitoring/
│   ├── spiders/
│   │   └── price_spider.py
│   ├── pipelines.py
│   ├── items.py
│   ├── settings.py
├── transformation/
│   ├── transform.py
├── dashboard/
│   ├── app.py
├── requirements.txt
└── README.md
```

## Documentation

[Github Pages](https://lvgalvao.github.io/ScrapyPriceMonitoring/)

## How to Use

To run web scraping:
```bash
scrapy crawl mercadolivre -o ../../data/data.jsonl
```

To run PANDAS, navigate to the SRC folder:
```bash
python transformation/main.py
```

To run Streamlit and build dashboards:
```bash
streamlit run app.py
```

## Modules

### Extraction

Quick Starter

Read documentation - [https://scrapy.org/](https://scrapy.org/)

---

This concludes the translated README for your ScrapyPriceMonitoring project. Let me know if there's anything else you need!