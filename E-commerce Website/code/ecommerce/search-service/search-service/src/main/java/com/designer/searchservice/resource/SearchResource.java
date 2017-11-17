package com.designer.searchservice.resource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;


@RestController
@RequestMapping("/rest/search")
public class SearchResource {
	
	@Autowired
	RestTemplate restTemplate;

	@GetMapping("/{productId}")
	public String getProduct(@PathVariable("productId") final String productId) {
		
		ResponseEntity<String> response = restTemplate.exchange("http://localhost:8301/rest/db/"+productId, HttpMethod.GET,null,
				new ParameterizedTypeReference<String>() {
				});
		return response.getBody();
	}
	
}
