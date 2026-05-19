# 🛒 E-commerce API

API RESTful de e-commerce desenvolvida para estudo de modelagem relacional, CRUDs e arquitetura backend utilizando FastAPI e MySQL.

## ⚙️ Tecnologias Utilizadas
### Backend
<p>
    <img
      src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white"/>
    <img src="https://img.shields.io/badge/-SQLModel-CC2927?style=flat&logo=databricks&logoColor=white"/>
</p>

### Banco de Dados
<img src="https://img.shields.io/badge/-MySQL-4479A1?style=flat&logo=mysql&logoColor=white"/>



### Ferramentas
<p>
    <img src="https://img.shields.io/badge/-Uvicorn-4051B5?style=flat&logo=uvicorn&logoColor=white"/>
     <img src="https://img.shields.io/badge/-Git-F05032?style=flat&logo=git&logoColor=white"/>
</p>


# 📁 Estrutura do Projeto
```
ecommerce/
├── app
│   ├── database.py
│   ├── deps
│   │   └── deps.py
│   ├── main.py
│   ├── models.py
│   ├── requirements.txt
│   └── routes
│       ├── avaliacoes
│       │   └── avaliacoes.py
│       ├── categorias
│       │   └── categorias.py
│       ├── enderecos
│       │   └── enderecos.py
│       ├── estoque
│       │   └── estoque.py
│       ├── pagamentos
│       │   └── pagamentos.py
│       ├── papeis
│       │   └── papeis.py
│       ├── pedidos
│       │   └── pedidos.py
│       ├── produtos
│       │   └── produtos.py
│       └── usuarios
│           └── usuarios.py
├── LICENSE
└── README.md

```