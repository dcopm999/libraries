from unittest import TestCase

from libraries.managers import Manager


class BaseManagerTestCase(TestCase):
    def setUp(self):
        self.item = {
            "uuid": "505282cf-d704-4b68-aad9-87f6f6000000",
            "country": "test",
            # "slug": "uzbekistan"
        }
        self.manager = Manager()

    def test_get_list(self):
        self.manager.create_item(self.item)
        self.manager.get_list()
        self.assertEqual(self.manager.code, 200)

    def test_delete_item(self):
        self.manager.create_item(self.item)
        self.manager.delete_item(self.item)
        self.assertEqual(self.manager.code, 204)

    def test_create_item(self):
        self.manager.delete_item(self.item)
        self.manager.create_item(self.item)
        self.assertEqual(self.manager.code, 200)

    def test_update_item(self):
        self.manager.create_item(self.item)
        self.manager.update_item(self.item)
        self.assertEqual(self.manager.code, 200)

    def test_update_or_create(self):
        self.manager.update_or_create(self.item)
        self.assertEqual(self.manager.code, 200)

    def test_get_item_by_uuid(self):
        self.manager.update_or_create(self.item)
        self.manager.get_item_by_uuid(self.item['uuid'])
        self.assertEqual(self.manager.code, 200)

    def tearDown(self):
        self.manager.delete_item(self.item)
