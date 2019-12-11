package com.how2java.service;

import java.util.List;

import com.how2java.entity.Category;

public interface CategoryService {
	List<Category> list();

	// int total();
	// List<Category> list(Page page);
	int add(Category category);

	int update(Category category);

	void delete(Category category);
	
	Category get(int id);

}
