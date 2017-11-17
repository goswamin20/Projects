package com.designer.dbservice.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.designer.dbservice.model.Product;

public interface ProductsRepository extends JpaRepository<Product, Integer>{

	 Product findByProductId(int productId);
}
