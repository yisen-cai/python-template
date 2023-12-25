from spiders.portal import Portal


class Test:
    portal = Portal()

    def test_run(self):
        assert True

    def test_get_app_tree(self):
        tree_nodes = self.portal.get_app_tree()
        assert len(tree_nodes) > 0
        assert 'build' == tree_nodes[0].app_tag

    def test_get_app_details(self):
        detail = self.portal.get_app_details("f_twell_domestic")
        assert 'pass' == detail.status

    def test_write_to_db(self):
        pass
        # detail = self.portal.get_app_details("f_twell_domestic")
        # self.portal.write_to_db([detail])
