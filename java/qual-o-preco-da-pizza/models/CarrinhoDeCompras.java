package models;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;
import java.util.Map.Entry;

public class CarrinhoDeCompras {
	ArrayList<Pizza> items = new ArrayList<Pizza>();

	public void adicionarItem(Pizza pizza) {
		items.add(pizza);
	}

	public float getValorTotal() {
		float valorTotal = 0;

		for (Pizza pizza : items) {
			valorTotal += pizza.getPreco();
		}

		return valorTotal;
	}

	public void imprimirQuantidadeDeIngredientesUtilizados() {
		HashMap<String, Integer> qtdPorIngrediente = new HashMap<String, Integer>();

		for (Pizza pizza : items) {
			HashMap<String, Integer> ingredientes = pizza.getIngredientes();

			for (String ingrediente : ingredientes.keySet()) {
				Integer valorAtual = qtdPorIngrediente.get(ingrediente);

				if (valorAtual == null) {
					qtdPorIngrediente.put(ingrediente, ingredientes.get(ingrediente));
					continue;
				}
				qtdPorIngrediente.put(ingrediente, valorAtual + ingredientes.get(ingrediente));
			}
		}

		for (Entry<String, Integer> ingrediente : qtdPorIngrediente.entrySet()) {
			System.out.println("Foram utilizados " + ingrediente.getValue() + " ingredientes de " + ingrediente.getKey());
		}
	}
}