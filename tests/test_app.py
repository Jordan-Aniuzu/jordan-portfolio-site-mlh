# tests/test_app.py

import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()

	def test_home(self):
		response = self.client.get("/")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>MLH PE Squad</title>" in html
		assert "Mahashri Ranjith Kumar" in html
		assert "Narottam Slawski" in html
		assert "Jordan Aniuzu" in html
		assert 'href="/maha"' in html
		assert 'href="/naro"' in html
		assert 'href="/jordan"' in html

	def test_jordan_page(self):
		response = self.client.get("/jordan")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>Jordan Aniuzu</title>" in html

	def test_timeline(self):
		response = self.client.get("/api/timeline_post")
		assert response.status_code == 200
		assert response.is_json
		json = response.get_json()
		assert "timeline_posts" in json
		assert len(json["timeline_posts"]) == 0

	def test_timeline_post_valid(self):
		response = self.client.post("/api/timeline_post", data={
			"name": "John Doe",
			"email": "john@example.com",
			"content": "Hello world, I'm John!"
		})
		json = response.get_json()
		assert response.status_code == 200
		assert json["name"] == "John Doe"
		assert json["email"] == "john@example.com"
		assert json["content"] == "Hello world, I'm John!"

	def test_malformed_timeline_post(self):
		response = self.client.post("/api/timeline_post", data={
			"email": "john@example.com",
			"content": "Hello world, I'm John!"
		})
		assert response.status_code == 400
		html = response.get_data(as_text=True)
		assert "Invalid name" in html

		response = self.client.post("/api/timeline_post", data={
			"name": "John Doe",
			"email": "john@example.com"
                })
		assert response.status_code == 400
		html = response.get_data(as_text=True)
		assert "Invalid content" in html

		response = self.client.post("/api/timeline_post", data={
			"name": "John Doe",
			"email": "not-valid-email",
			"content": "Hello world, I'm John!"
		})
		assert response.status_code == 400
		html = response.get_data(as_text=True)
		assert "Invalid email" in html


	def test_timeline_page(self):
		response = self.client.get("/timeline")
		assert response.status_code == 200
		html = response.get_data(as_text=True)
		assert "<title>Timeline</title>" in html
