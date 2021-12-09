Module(
    body=[
        Import(
            names=[
                alias(name='sys', asname=None),
                alias(name='os', asname=None),
            ],
        ),
        Assign(
            targets=[Name(id='extensions', ctx=Store())],
            value=List(
                elts=[Constant(value='sphinx.ext.todo', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='templates_path', ctx=Store())],
            value=List(
                elts=[Constant(value='_templates', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='source_suffix', ctx=Store())],
            value=Constant(value='.rst', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='master_doc', ctx=Store())],
            value=Constant(value='index', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='project', ctx=Store())],
            value=Constant(value='py.js', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='copyright', ctx=Store())],
            value=Constant(value='2012, Xavier Morel', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='version', ctx=Store())],
            value=Constant(value='0.6', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='release', ctx=Store())],
            value=Constant(value='0.6', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='exclude_patterns', ctx=Store())],
            value=List(
                elts=[Constant(value='_build', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='default_domain', ctx=Store())],
            value=Constant(value='js', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='pygments_style', ctx=Store())],
            value=Constant(value='sphinx', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='highlight_language', ctx=Store())],
            value=Constant(value='javascript', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='html_theme', ctx=Store())],
            value=Constant(value='default', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='html_static_path', ctx=Store())],
            value=List(
                elts=[Constant(value='_static', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='htmlhelp_basename', ctx=Store())],
            value=Constant(value='pyjsdoc', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='latex_elements', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='latex_documents', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='index', kind=None),
                            Constant(value='pyjs.tex', kind=None),
                            Constant(value='py.js Documentation', kind='u'),
                            Constant(value='Xavier Morel', kind='u'),
                            Constant(value='manual', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='man_pages', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='index', kind=None),
                            Constant(value='pyjs', kind=None),
                            Constant(value='py.js Documentation', kind='u'),
                            List(
                                elts=[Constant(value='Xavier Morel', kind='u')],
                                ctx=Load(),
                            ),
                            Constant(value=1, kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='texinfo_documents', ctx=Store())],
            value=List(
                elts=[
                    Tuple(
                        elts=[
                            Constant(value='index', kind=None),
                            Constant(value='pyjs', kind=None),
                            Constant(value='py.js Documentation', kind='u'),
                            Constant(value='Xavier Morel', kind='u'),
                            Constant(value='pyjs', kind=None),
                            Constant(value='One line description of project.', kind=None),
                            Constant(value='Miscellaneous', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
