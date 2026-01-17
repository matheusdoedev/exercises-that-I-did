package models;

import java.util.HashMap;

public class Pizza {
	private HashMap<String, Integer> ingredientes = new HashMap<String, Integer>();

	public void adicionaIngrediente(String ingrediente) {
		Integer valorAtual = ingredientes.get(ingrediente);

		if (valorAtual == null) {
			contabilizaIngrediente(ingrediente, 1);
			return;
		}

		Integer novoValor = valorAtual + 1;

		contabilizaIngrediente(ingrediente, novoValor);
	}

	public HashMap<String, Integer> getIngredientes() {
		return this.ingredientes;
	}

	private void contabilizaIngrediente(String ingrediente, Integer novoValor) {
		ingredientes.put(ingrediente, novoValor);
	}

	public float getPreco() {
		int quantidadeDeIngredientes = 0;

		for (int qtdDoIngrediente : ingredientes.values()) {
			quantidadeDeIngredientes += qtdDoIngrediente;
		}

		return definirPreco(quantidadeDeIngredientes);
	}

	private float definirPreco(int quantidadeDeIngredientes) {
		if (quantidadeDeIngredientes <= 2) {
			return 15;
		} else if (quantidadeDeIngredientes >= 3 || quantidadeDeIngredientes <= 5) {
			return 20;
		} else {
			return 23;
		}
	}
}