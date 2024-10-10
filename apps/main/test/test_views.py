import json

from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from apps.main import models
from apps.user.auth import models as auth_models


class TestListCatView(APITestCase):
    """Testing the ListCatView endpoint methods"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.token = auth_models.JWTToken.objects.get(id=1)

        cls.client = APIClient()

        cls.path = reverse("cat-list")

        cls.valid_data = {"name": "cat", "age": 11, "breed": "11", "hairiness": "BALD"}
        cls.invalid_data = {"name": "cat", "age": "11q", "breed": "11", "hairiness": "BALT"}
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        response = self.client.get(self.path)
        assert response.status_code == 200, response.status_code
        assert response.data["count"] == 1, response.data["count"]
        assert response.data["results"][0]["age"] == 12312, response.data["results"][0]["age"]
    
    def test_post_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)

        # invalid - invalid data
        with self.assertLogs(level="WARNING"):
            invalid_resposne = self.client.post(path=self.path, data=self.invalid_data)
        detail_error = json.loads(invalid_resposne.content)
        assert invalid_resposne.status_code == 400, invalid_resposne.status_code
        assert ["A valid integer is required."] == detail_error["age"], detail_error
        assert ['"BALT" is not a valid choice.'] == detail_error["hairiness"], detail_error

        # valid
        valid_resposne = self.client.post(path=self.path, data=self.valid_data)
        assert valid_resposne.status_code == 201, valid_resposne.status_code


class TestCatView(APITestCase):
    """Testing the CatView endpoint methods"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.token = auth_models.JWTToken.objects.get(id=1)

        cls.client = APIClient()
        cls.path = reverse("cat-detail", kwargs={"id": 1})

        cls.valid_data = {"name": "cat1", "age": 111, "breed": "11", "hairiness": "BALD"}
        cls.invalid_data = {"name": "cat", "age": "11q", "breed": "11", "hairiness": "BALT"}
    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        response = self.client.get(self.path)
        assert response.status_code == 200, response.status_code
        assert response.data["id"]== 1, response.data
        assert response.data["age"] == 12312, response.data
    
    def test_put_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        valid_resposne = self.client.put(path=self.path, data=self.valid_data)
        assert valid_resposne.status_code == 200, valid_resposne.status_code

        with self.assertLogs(level="WARNING"):
            invalid_resposne = self.client.put(path=self.path, data=self.invalid_data)
        
        assert invalid_resposne.status_code == 400, invalid_resposne.status_code


class TestListChatView(APITestCase):
    """Testing the ListChatView endpoint methods"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.token = auth_models.JWTToken.objects.get(id=1)

        cls.client = APIClient()
        cls.path = reverse("chat-list")

    
    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        response = self.client.get(self.path)
        assert response.status_code == 200, response.status_code
        assert response.data["count"] == 2, response.data["count"]
    
    def test_post_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)

        with self.assertLogs(level="WARNING"):
            response = self.client.post(self.path)
        detail_error = json.loads(response.content)["detail"]
        assert response.status_code == 405, response.status_code
        assert 'Method "POST" not allowed.' == detail_error, detail_error


class TestChatView(APITestCase):
    """Testing the ChatView endpoint methods"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.token = auth_models.JWTToken.objects.get(id=1)

        cls.client = APIClient()
        cls.path = reverse("chat-detail", kwargs={"id": 1})

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        response = self.client.get(self.path)
        assert response.status_code == 200, response.status_code
        assert response.data["id"]== 1, response.data
        assert response.data["users"][0] == 1, response.data
    
    def test_put_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)

        with self.assertLogs(level="WARNING"):
            response = self.client.put(self.path)
        detail_error = json.loads(response.content)["detail"]
        assert response.status_code == 405, response.status_code
        assert 'Method "PUT" not allowed.' == detail_error, detail_error


class TestCreateChatView(APITestCase):
    """Testing the create_chat_view endpoint methods"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.token = auth_models.JWTToken.objects.get(id=1)
        cls.token_1 = auth_models.JWTToken.objects.get(id=3)

        cls.client = APIClient()
        cls.path = reverse("create_chat", kwargs={"user_id": 2})
        cls.path_1 = reverse("create_chat", kwargs={"user_id": 2})

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
    
    def test_get_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)
        response = self.client.get(self.path)
        count_1 = models.Chat.objects.count()
        assert response.status_code == 302, response.status_code
        assert count_1 == 2, count_1

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token_1.access_token)
        response = self.client.get(self.path_1)
        count_1 = models.Chat.objects.count()
        assert response.status_code == 302, response.status_code
        assert count_1 == 3, count_1
    
    def test_post_method(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.access_token)

        with self.assertLogs(level="WARNING"):
            response = self.client.post(self.path)
        detail_error = json.loads(response.content)["detail"]
        assert response.status_code == 405, response.status_code
        assert 'Method "POST" not allowed.' == detail_error, detail_error
