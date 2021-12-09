Module(
    body=[
        ImportFrom(
            module='setuptools',
            names=[
                alias(name='find_packages', asname=None),
                alias(name='setup', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='os.path',
            names=[
                alias(name='join', asname=None),
                alias(name='dirname', asname=None),
            ],
            level=0,
        ),
        Expr(
            value=Call(
                func=Name(id='exec', ctx=Load()),
                args=[
                    Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='open', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='join', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='dirname', ctx=Load()),
                                                args=[Name(id='__file__', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(value='odoo', kind=None),
                                            Constant(value='release.py', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value='rb', kind=None),
                                ],
                                keywords=[],
                            ),
                            attr='read',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
        ),
        Assign(
            targets=[Name(id='lib_name', ctx=Store())],
            value=Constant(value='odoo', kind=None),
            type_comment=None,
        ),
        Expr(
            value=Call(
                func=Name(id='setup', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        arg='name',
                        value=Constant(value='odoo', kind=None),
                    ),
                    keyword(
                        arg='version',
                        value=Name(id='version', ctx=Load()),
                    ),
                    keyword(
                        arg='description',
                        value=Name(id='description', ctx=Load()),
                    ),
                    keyword(
                        arg='long_description',
                        value=Name(id='long_desc', ctx=Load()),
                    ),
                    keyword(
                        arg='url',
                        value=Name(id='url', ctx=Load()),
                    ),
                    keyword(
                        arg='author',
                        value=Name(id='author', ctx=Load()),
                    ),
                    keyword(
                        arg='author_email',
                        value=Name(id='author_email', ctx=Load()),
                    ),
                    keyword(
                        arg='classifiers',
                        value=ListComp(
                            elt=Name(id='c', ctx=Load()),
                            generators=[
                                comprehension(
                                    target=Name(id='c', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='classifiers', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                    ifs=[Name(id='c', ctx=Load())],
                                    is_async=0,
                                ),
                            ],
                        ),
                    ),
                    keyword(
                        arg='license',
                        value=Name(id='license', ctx=Load()),
                    ),
                    keyword(
                        arg='scripts',
                        value=List(
                            elts=[Constant(value='setup/odoo', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        arg='packages',
                        value=Call(
                            func=Name(id='find_packages', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    keyword(
                        arg='package_dir',
                        value=Dict(
                            keys=[
                                BinOp(
                                    left=Constant(value='%s', kind=None),
                                    op=Mod(),
                                    right=Name(id='lib_name', ctx=Load()),
                                ),
                            ],
                            values=[Constant(value='odoo', kind=None)],
                        ),
                    ),
                    keyword(
                        arg='include_package_data',
                        value=Constant(value=True, kind=None),
                    ),
                    keyword(
                        arg='install_requires',
                        value=List(
                            elts=[
                                Constant(value='babel >= 1.0', kind=None),
                                Constant(value='decorator', kind=None),
                                Constant(value='docutils', kind=None),
                                Constant(value='gevent', kind=None),
                                Constant(value='html2text', kind=None),
                                Constant(value='idna', kind=None),
                                Constant(value='Jinja2', kind=None),
                                Constant(value='lxml', kind=None),
                                Constant(value='libsass', kind=None),
                                Constant(value='mock', kind=None),
                                Constant(value='ofxparse', kind=None),
                                Constant(value='passlib', kind=None),
                                Constant(value='pillow', kind=None),
                                Constant(value='polib', kind=None),
                                Constant(value='psutil', kind=None),
                                Constant(value='psycopg2 >= 2.2', kind=None),
                                Constant(value='pydot', kind=None),
                                Constant(value='pyopenssl', kind=None),
                                Constant(value='pypdf2', kind=None),
                                Constant(value='pyserial', kind=None),
                                Constant(value='python-dateutil', kind=None),
                                Constant(value='python-stdnum', kind=None),
                                Constant(value='pytz', kind=None),
                                Constant(value='pyusb >= 1.0.0b1', kind=None),
                                Constant(value='qrcode', kind=None),
                                Constant(value='reportlab', kind=None),
                                Constant(value='requests', kind=None),
                                Constant(value='zeep', kind=None),
                                Constant(value='vobject', kind=None),
                                Constant(value='werkzeug', kind=None),
                                Constant(value='xlsxwriter', kind=None),
                                Constant(value='xlwt', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        arg='python_requires',
                        value=Constant(value='>=3.7', kind=None),
                    ),
                    keyword(
                        arg='extras_require',
                        value=Dict(
                            keys=[
                                Constant(value='ldap', kind=None),
                                Constant(value='SSL', kind=None),
                            ],
                            values=[
                                List(
                                    elts=[Constant(value='python-ldap', kind=None)],
                                    ctx=Load(),
                                ),
                                List(
                                    elts=[Constant(value='pyopenssl', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                        ),
                    ),
                    keyword(
                        arg='tests_require',
                        value=List(
                            elts=[Constant(value='freezegun', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                ],
            ),
        ),
    ],
    type_ignores=[],
)
