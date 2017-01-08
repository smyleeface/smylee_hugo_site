import unittest
import os
import os.path
import re


class TestCheckMarkdown(unittest.TestCase):

    @staticmethod
    def create_regex(required_front_matter, type=None):
        regex_str = ''
        toml = required_front_matter['toml']

        regex_str += toml['format_identifier']
        regex_str += toml['title']
        regex_str += toml['date']
        regex_str += toml['toc']
        regex_str += toml['draft']
        if type == 'post':
            regex_str += toml['categories']
            regex_str += toml['tags']
        regex_str += required_front_matter['any_field']
        regex_str += toml['format_identifier']

        return regex_str

    def test_hugo_front_matter(self):

        required_front_matter = {
            'any_field': '((.|\n)*)',
            'toml': {
                'title': '(title = ".*"\n)',
                'date': '(date = "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}"\n)',
                'categories': '(categories = \[".*"\]\n)',
                'tags': '(tags = \[".*"\]\n)',
                'toc': '(toc = (true|false)\n)',
                'draft': '(draft = (true|false)\n)',
                'format_identifier': '([\+]{3}\n)'
            }
            # ,
            # 'yaml': {
            #     'title': '(title: ".*")',
            #     'date': '(date: "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}"\n)',
            #     'categories': '(categories: \[".*"\])',
            #     'tags': '(tags: \[".*"\])',
            #     'toc': '(toc: true|false)',
            #     'draft': '(draft: true|false)',
            #     'format_identifier': '([\-]{3}\n)'
            # },
            # 'json': {
            #     'title': '(title = ".*")',
            #     'date': '(date = "\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}-\d{2}:\d{2}"\n)',
            #     'categories': '(categories = \[".*"\])',
            #     'tags': '(tags = \[".*"\])',
            #     'toc': '(toc = true|false)',
            #     'draft': '(draft = true|false)',
            #     'format_identifiers': {
            #         '{': '([\{]{1}\n)',
            #         '}': '([\}]{1}\n)'
            #     }
            # }
        }

        regex_post_str = self.create_regex(required_front_matter, 'post')
        regex_default_str = self.create_regex(required_front_matter, 'default')
        path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

        list_of_post_files = {}
        list_of_other_files = {}
        list_of_post_file_issues = []
        list_of_other_file_issues = []
        for (dirpath, dirnames, filenames) in os.walk('{0}/content'.format(path)):
            # print dirpath
            # print dirnames
            for filename in filenames:
                if filename.endswith('.md') and dirpath.find('/content/post') > 0:
                    list_of_post_files[filename] = os.sep.join([dirpath, filename])
                elif filename.endswith('.md'):
                    list_of_other_files[filename] = os.sep.join([dirpath, filename])

        for md_file in list_of_post_files.itervalues():
            with open(md_file, 'r') as md_file_cur:
                # print "post"
                all_md_lines = md_file_cur.read()
                m = re.match(regex_post_str, all_md_lines)
                if m is None:
                    list_of_post_file_issues.append(md_file)
                # print '{0}: {1}'.format(md_file, m)

        for md_file in list_of_other_files.itervalues():
            with open(md_file, 'r') as md_file_cur:
                # print "other"
                all_md_lines = md_file_cur.read()
                m = re.match(regex_default_str, all_md_lines)
                if m is None:
                    list_of_other_file_issues.append(md_file)
                    # print '{0}: {1}'.format(md_file, m)

        self.assertFalse(list_of_post_file_issues, "There are issues with the following post files: {0}".format(', '.join(list_of_post_file_issues)))
        self.assertFalse(list_of_other_file_issues, "There are issues with the following other files: {0}".format(', '.join(list_of_post_file_issues)))

if __name__ == '__main__':
    unittest.main()
