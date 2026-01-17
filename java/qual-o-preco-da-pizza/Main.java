import models.*;

public class Main {
	public static void main(String[] args) {
		CarrinhoDeCompras carrinhoDeCompras = new CarrinhoDeCompras();
		Pizza pizza1 = new Pizza();
		Pizza pizza2 = new Pizza();
		Pizza pizza3 = new Pizza();

		pizza1.adicionaIngrediente("calabresa");
		pizza1.adicionaIngrediente("cebola");
		pizza1.adicionaIngrediente("oregáno");
		pizza2.adicionaIngrediente("frango");
		pizza2.adicionaIngrediente("catupiry");
		pizza3.adicionaIngrediente("bacon");
		pizza3.adicionaIngrediente("ovo");
		pizza3.adicionaIngrediente("oregáno");
		pizza3.adicionaIngrediente("calabresa");
		pizza3.adicionaIngrediente("cebola");
		carrinhoDeCompras.adicionarItem(pizza1);
		carrinhoDeCompras.adicionarItem(pizza2);
		carrinhoDeCompras.adicionarItem(pizza3);
		System.out.println("O valor total no carrinho de compras é de: R$ " + String.format("%.2f", carrinhoDeCompras.getValorTotal()));
		carrinhoDeCompras.imprimirQuantidadeDeIngredientesUtilizados();
	}
}
