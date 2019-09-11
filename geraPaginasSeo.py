# -*- coding: utf-8 -*-
import pandas as pd
def criar(arquivo):
    x = pd.read_excel(arquivo, encoding = 'utf-8')
    for i in x.index:
        print(x['URL'][i])
        arquivoPhp = open('{}.php'.format(x['URL'][i]), 'w', encoding='utf-8')
        arquivoPhp.write(conteudoPadrao(x['H1'][i],x['URL'][i]))
def conteudoPadrao(titulo, url):
    txt = f'''<?php include 'inc/inc.seo.php'; ?>
</head>
<body>
  <!--[if lte IE 9]>
    <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
  <![endif]-->

  <?php include 'inc/inc.header.php'; ?>
  <main class="internas seo">
    <section class="banner">
      <h1 class="title">{titulo}</h1>
    </section>
    <section class="container">
      <div class="row">
          <div class="col-md-6">
              <img src="img/internas/seo/{url}.jpg" alt="{titulo}" title="{titulo}">
          </div>
          <div class="col-md-6">
              
          </div>
        </div>
    </section>
    <?php include 'inc/inc.footer.php'; ?>
    <?php include 'inc/inc.js.php'; ?>
</main>
</body>

</html>'''
    return txt