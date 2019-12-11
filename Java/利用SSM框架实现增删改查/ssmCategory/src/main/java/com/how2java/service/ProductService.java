package com.how2java.service;

import java.util.List;

import com.how2java.entity.Product;

public interface ProductService {
	int add(Product p);
	List<Product> list();
	void delete(Product product);
	Product get(int id);
	int update(Product p);
}
