from rest_framework.test import APITestCase

from apps.main import models


class TestCatModel(APITestCase):
    """Testing Cat model"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.cat_1 = models.Cat.objects.get(id=1)
        cls.cat_2 = models.Cat.objects.get(id=2)
            
    def test__str__method(self):
        """Testing __str__ method"""

        resposne = self.cat_1.__str__()
        assert resposne == "qweqwe", resposne

        resposne = self.cat_2.__str__()
        assert resposne == "qweqwe", resposne
    
    def test_get_absolute_url_method(self):
        """Testing get_absolute_url method"""

        response = self.cat_1.get_absolute_url()
        assert response == "/api/v1/cats/1/", response

        response = self.cat_2.get_absolute_url()
        assert response == "/api/v1/cats/2/", response


class TestChatModel(APITestCase):
    """Testing Chat model"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.chat_1 = models.Chat.objects.get(id=1)
        cls.chat_2 = models.Chat.objects.get(id=2)
            
    def test__str__method(self):
        """Testing __str__ method"""

        resposne = self.chat_1.__str__()
        assert resposne == "1", resposne

        resposne = self.chat_2.__str__()
        assert resposne == "2", resposne
    
    def test_get_absolute_url_method(self):
        """Testing get_absolute_url method"""

        response = self.chat_1.get_absolute_url()
        assert response == "/api/v1/chats/1/", response

        response = self.chat_2.get_absolute_url()
        assert response == "/api/v1/chats/2/", response


class TestMessageModel(APITestCase):
    """Testing Message model"""

    fixtures = ["./config/test/test_data.json"]

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

        cls.message_1 = models.Message.objects.get(id=1)
        cls.message_2 = models.Message.objects.get(id=2)
            
    def test__str__method(self):
        """Testing __str__ method"""

        resposne = self.message_1.__str__()
        assert resposne == "1", resposne

        resposne = self.message_2.__str__()
        assert resposne == "2", resposne
