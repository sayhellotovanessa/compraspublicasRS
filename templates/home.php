<section id="contentcontainer"> 
	<section id="intro">
		<h2 class="intro">
			Consulte valores de compras realizadas pelo <strong>governo</strong> através de um simples formulário. <span class="sub"> É simples, né?</span>
		</h2>
		<br/>
		
			<div id="form">
				<input type="text" id="texto-busca" placeholder="Digite aqui sua palavra-chave...">

				<select id="tipo-busca">
		  		<option value="0">Palavra-chave</option>
		  		<option value="1">CNPJ</option>
		  		<option value="2">Empresa vencedora</option>
		  		<option value="3">Data de publicação</option>
				</select>
				
				<a class="submit-button search-button" href="javascript:void(0);">Pesquisar</a>
				<br/> 
				<span class="exemplo-pesquisa">
					<strong>Exemplo:</strong> suprimentos informática, aquisição de vestuário em fevereiro de 2011, etc...
				</span>
				
				<div id="load-box">
					<img src="<?=DIR_SITE?>imgs/ajax-loader.gif">
					<br/>
					<span class="bigRed">Buscando...<span>
				</div>
				<div id="erro-box" class="bigRed">
					<span class="doh">D'Oh!</span>
				</div>
			</div>
	
    				
	</section>

	<section id="data-table"> 
		<h2 class="work">Minha Consulta</h2>
	
			<table cellpadding="" cellspacing="" summary="" border="" bordercolor="" align="default" width="px" height="px">
				<tr>
					<th>Descrição</th>
					<th>Portal</th>
					<th>Licitação</th>
					<th>Empresa Vencedora</th>
					<th>CNPJ</th>
					<th>Valor</th>
					<th>Quantidade</th>
					<th>Data</th>
					<th></th>
				</tr>
				<tr>
					<td>Materiais e suprimentos para informática.</td>
					<td>CECOM</td>
					<td>1</td>
					<td>LEXBEMARK</td>
					<td>03328413000198</td>
					<td>R$ 6470</td>
					<td>2</td>
					<td>04/01/2011</td>
					<td><a href="oi.html" rel="lightbox">Completo</a></td>
				</tr>
				<tr>
					<td>Materiais e suprimentos para informática.</td>
					<td>CECOM</td>
					<td>1</td>
					<td>LEXBEMARK</td>
					<td>03328413000198</td>
					<td>R$ 6470</td>
					<td>2</td>
					<td>04/01/2011</td>
					<td><a href="oi.html#" rel="bump" rel="400-300">Completo</a></td>
				</tr>
				<tr>
					<td>Materiais e suprimentos para informática.</td>
					<td>CECOM</td>
					<td>1</td>
					<td>LEXBEMARK</td>
					<td>03328413000198</td>
					<td>R$ 6470</td>
					<td>2</td>
					<td>04/01/2011</td>
					<td><a href="#">Completo</a></td>
				</tr>
				<tr>
					<td>Materiais e suprimentos para informática.</td>
					<td>CECOM</td>
					<td>1</td>
					<td>LEXBEMARK</td>
					<td>03328413000198</td>
					<td>R$ 6470</td>
					<td>2</td>
					<td>04/01/2011</td>
					<td><a href="#">Completo</a></td>
				</tr>
			</table> 
		
			<share>
				<a style="margin-right:50px;" href="https://twitter.com/share" class="twitter-share-button" data-text="#wehateit I really hate it:" data-count="horizontal">Tweet</a>
				<script type="text/javascript" src="//platform.twitter.com/widgets.js"></script>
				<div class="fb-send" data-href="http://example.com" data-font="lucida grande" data-colorscheme="dark"></div>
				<br>
			</share>		
		</section>
    			
		<section id="about"> 
			<h2 class="about">Sobre o projeto</h2>
			<p>Consulte, compartilhe e comente os dados que você procurou.  </p>
			<p>Consultas Públicas é um projeto de licença livre, desenvolvido por Vanessa Guedes (<a href="http://twitter.com/nessoila">@nessoila</a>) e Murilo Prestes (<a href="http://twitter.com/MacLovinBr">@MacLovinBr</a>) em julho de 2012, como projeto do primeiro concurso Decoders, da W3C, realizado durante o FISL 13. <br> Todo o projeto fio escrito em open source, e você pode ver e baixar o código na página do projeto no github.</p>	
    </section>

		<section id="api">
			<h2 class="api">API</h2>
				<p>	
					Todas as consultas de dados de compras homologadas poderá ser feita através de uma API REST livre, tanto para utilização em outros aplicativos quanto para colaboração com novas tabelas de dados de outros estados no nosso <a href="https://github.com/nessoila/compraspublicasRS/tree/master/dados">Github</a>.
					
					<p>
						<strong>Métodos:</strong>
						<br/>
						
						<span class="code">
							<?=DIR_SITE?>api/consulta/palavraChave/{termos para pesquisa}
						</span>
						<strong class="small">Pesquisa por palavra chave</strong>
						<br/>
						<span class="code">
							<?=DIR_SITE?>api/consulta/cnpj/{cnpj sem ponto, barra e hífen}
						</span>
						<strong class="small">Pesquisa por CNPJ da empresa vencedora</strong>
						<br/>
						<span class="code">
							<?=DIR_SITE?>api/consulta/empresaVencedora/{razão social}
						</span>
						<strong class="small">Pesquisa por razão social da empresa vencedora</strong>
						<br/>
						<span class="code">
							<?=DIR_SITE?>api/consulta/data/{data invertida aaaammdd sem barras}
						</span>
						<strong class="small">Pesquisa por data de publicação</strong>
					</p>
				</p>
		</section>
	</section>