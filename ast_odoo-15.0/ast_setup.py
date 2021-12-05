Module(
    body=[
        ImportFrom(
            lineno=4,
            col_offset=0,
            end_lineno=4,
            end_col_offset=43,
            module='setuptools',
            names=[
                alias(name='find_packages', asname=None),
                alias(name='setup', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            lineno=5,
            col_offset=0,
            end_lineno=5,
            end_col_offset=33,
            module='os.path',
            names=[
                alias(name='join', asname=None),
                alias(name='dirname', asname=None),
            ],
            level=0,
        ),
        Expr(
            lineno=8,
            col_offset=0,
            end_lineno=8,
            end_col_offset=70,
            value=Call(
                lineno=8,
                col_offset=0,
                end_lineno=8,
                end_col_offset=70,
                func=Name(lineno=8, col_offset=0, end_lineno=8, end_col_offset=4, id='exec', ctx=Load()),
                args=[
                    Call(
                        lineno=8,
                        col_offset=5,
                        end_lineno=8,
                        end_col_offset=69,
                        func=Attribute(
                            lineno=8,
                            col_offset=5,
                            end_lineno=8,
                            end_col_offset=67,
                            value=Call(
                                lineno=8,
                                col_offset=5,
                                end_lineno=8,
                                end_col_offset=62,
                                func=Name(lineno=8, col_offset=5, end_lineno=8, end_col_offset=9, id='open', ctx=Load()),
                                args=[
                                    Call(
                                        lineno=8,
                                        col_offset=10,
                                        end_lineno=8,
                                        end_col_offset=55,
                                        func=Name(lineno=8, col_offset=10, end_lineno=8, end_col_offset=14, id='join', ctx=Load()),
                                        args=[
                                            Call(
                                                lineno=8,
                                                col_offset=15,
                                                end_lineno=8,
                                                end_col_offset=32,
                                                func=Name(lineno=8, col_offset=15, end_lineno=8, end_col_offset=22, id='dirname', ctx=Load()),
                                                args=[Name(lineno=8, col_offset=23, end_lineno=8, end_col_offset=31, id='__file__', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Constant(lineno=8, col_offset=34, end_lineno=8, end_col_offset=40, value='odoo', kind=None),
                                            Constant(lineno=8, col_offset=42, end_lineno=8, end_col_offset=54, value='release.py', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(lineno=8, col_offset=57, end_lineno=8, end_col_offset=61, value='rb', kind=None),
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
            lineno=9,
            col_offset=0,
            end_lineno=9,
            end_col_offset=17,
            targets=[Name(lineno=9, col_offset=0, end_lineno=9, end_col_offset=8, id='lib_name', ctx=Store())],
            value=Constant(lineno=9, col_offset=11, end_lineno=9, end_col_offset=17, value='odoo', kind=None),
            type_comment=None,
        ),
        Expr(
            lineno=11,
            col_offset=0,
            end_lineno=67,
            end_col_offset=1,
            value=Call(
                lineno=11,
                col_offset=0,
                end_lineno=67,
                end_col_offset=1,
                func=Name(lineno=11, col_offset=0, end_lineno=11, end_col_offset=5, id='setup', ctx=Load()),
                args=[],
                keywords=[
                    keyword(
                        lineno=12,
                        col_offset=4,
                        end_lineno=12,
                        end_col_offset=15,
                        arg='name',
                        value=Constant(lineno=12, col_offset=9, end_lineno=12, end_col_offset=15, value='odoo', kind=None),
                    ),
                    keyword(
                        lineno=13,
                        col_offset=4,
                        end_lineno=13,
                        end_col_offset=19,
                        arg='version',
                        value=Name(lineno=13, col_offset=12, end_lineno=13, end_col_offset=19, id='version', ctx=Load()),
                    ),
                    keyword(
                        lineno=14,
                        col_offset=4,
                        end_lineno=14,
                        end_col_offset=27,
                        arg='description',
                        value=Name(lineno=14, col_offset=16, end_lineno=14, end_col_offset=27, id='description', ctx=Load()),
                    ),
                    keyword(
                        lineno=15,
                        col_offset=4,
                        end_lineno=15,
                        end_col_offset=30,
                        arg='long_description',
                        value=Name(lineno=15, col_offset=21, end_lineno=15, end_col_offset=30, id='long_desc', ctx=Load()),
                    ),
                    keyword(
                        lineno=16,
                        col_offset=4,
                        end_lineno=16,
                        end_col_offset=11,
                        arg='url',
                        value=Name(lineno=16, col_offset=8, end_lineno=16, end_col_offset=11, id='url', ctx=Load()),
                    ),
                    keyword(
                        lineno=17,
                        col_offset=4,
                        end_lineno=17,
                        end_col_offset=17,
                        arg='author',
                        value=Name(lineno=17, col_offset=11, end_lineno=17, end_col_offset=17, id='author', ctx=Load()),
                    ),
                    keyword(
                        lineno=18,
                        col_offset=4,
                        end_lineno=18,
                        end_col_offset=29,
                        arg='author_email',
                        value=Name(lineno=18, col_offset=17, end_lineno=18, end_col_offset=29, id='author_email', ctx=Load()),
                    ),
                    keyword(
                        lineno=19,
                        col_offset=4,
                        end_lineno=19,
                        end_col_offset=57,
                        arg='classifiers',
                        value=ListComp(
                            lineno=19,
                            col_offset=16,
                            end_lineno=19,
                            end_col_offset=57,
                            elt=Name(lineno=19, col_offset=17, end_lineno=19, end_col_offset=18, id='c', ctx=Load()),
                            generators=[
                                comprehension(
                                    target=Name(lineno=19, col_offset=23, end_lineno=19, end_col_offset=24, id='c', ctx=Store()),
                                    iter=Call(
                                        lineno=19,
                                        col_offset=28,
                                        end_lineno=19,
                                        end_col_offset=51,
                                        func=Attribute(
                                            lineno=19,
                                            col_offset=28,
                                            end_lineno=19,
                                            end_col_offset=45,
                                            value=Name(lineno=19, col_offset=28, end_lineno=19, end_col_offset=39, id='classifiers', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(lineno=19, col_offset=46, end_lineno=19, end_col_offset=50, value='\n', kind=None)],
                                        keywords=[],
                                    ),
                                    ifs=[Name(lineno=19, col_offset=55, end_lineno=19, end_col_offset=56, id='c', ctx=Load())],
                                    is_async=0,
                                ),
                            ],
                        ),
                    ),
                    keyword(
                        lineno=20,
                        col_offset=4,
                        end_lineno=20,
                        end_col_offset=19,
                        arg='license',
                        value=Name(lineno=20, col_offset=12, end_lineno=20, end_col_offset=19, id='license', ctx=Load()),
                    ),
                    keyword(
                        lineno=21,
                        col_offset=4,
                        end_lineno=21,
                        end_col_offset=26,
                        arg='scripts',
                        value=List(
                            lineno=21,
                            col_offset=12,
                            end_lineno=21,
                            end_col_offset=26,
                            elts=[Constant(lineno=21, col_offset=13, end_lineno=21, end_col_offset=25, value='setup/odoo', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        lineno=22,
                        col_offset=4,
                        end_lineno=22,
                        end_col_offset=28,
                        arg='packages',
                        value=Call(
                            lineno=22,
                            col_offset=13,
                            end_lineno=22,
                            end_col_offset=28,
                            func=Name(lineno=22, col_offset=13, end_lineno=22, end_col_offset=26, id='find_packages', ctx=Load()),
                            args=[],
                            keywords=[],
                        ),
                    ),
                    keyword(
                        lineno=23,
                        col_offset=4,
                        end_lineno=23,
                        end_col_offset=41,
                        arg='package_dir',
                        value=Dict(
                            lineno=23,
                            col_offset=16,
                            end_lineno=23,
                            end_col_offset=41,
                            keys=[
                                BinOp(
                                    lineno=23,
                                    col_offset=17,
                                    end_lineno=23,
                                    end_col_offset=32,
                                    left=Constant(lineno=23, col_offset=17, end_lineno=23, end_col_offset=21, value='%s', kind=None),
                                    op=Mod(),
                                    right=Name(lineno=23, col_offset=24, end_lineno=23, end_col_offset=32, id='lib_name', ctx=Load()),
                                ),
                            ],
                            values=[Constant(lineno=23, col_offset=34, end_lineno=23, end_col_offset=40, value='odoo', kind=None)],
                        ),
                    ),
                    keyword(
                        lineno=24,
                        col_offset=4,
                        end_lineno=24,
                        end_col_offset=29,
                        arg='include_package_data',
                        value=Constant(lineno=24, col_offset=25, end_lineno=24, end_col_offset=29, value=True, kind=None),
                    ),
                    keyword(
                        lineno=25,
                        col_offset=4,
                        end_lineno=58,
                        end_col_offset=5,
                        arg='install_requires',
                        value=List(
                            lineno=25,
                            col_offset=21,
                            end_lineno=58,
                            end_col_offset=5,
                            elts=[
                                Constant(lineno=26, col_offset=8, end_lineno=26, end_col_offset=22, value='babel >= 1.0', kind=None),
                                Constant(lineno=27, col_offset=8, end_lineno=27, end_col_offset=19, value='decorator', kind=None),
                                Constant(lineno=28, col_offset=8, end_lineno=28, end_col_offset=18, value='docutils', kind=None),
                                Constant(lineno=29, col_offset=8, end_lineno=29, end_col_offset=16, value='gevent', kind=None),
                                Constant(lineno=30, col_offset=8, end_lineno=30, end_col_offset=19, value='html2text', kind=None),
                                Constant(lineno=31, col_offset=8, end_lineno=31, end_col_offset=14, value='idna', kind=None),
                                Constant(lineno=32, col_offset=8, end_lineno=32, end_col_offset=16, value='Jinja2', kind=None),
                                Constant(lineno=33, col_offset=8, end_lineno=33, end_col_offset=14, value='lxml', kind=None),
                                Constant(lineno=34, col_offset=8, end_lineno=34, end_col_offset=17, value='libsass', kind=None),
                                Constant(lineno=35, col_offset=8, end_lineno=35, end_col_offset=14, value='mock', kind=None),
                                Constant(lineno=36, col_offset=8, end_lineno=36, end_col_offset=18, value='ofxparse', kind=None),
                                Constant(lineno=37, col_offset=8, end_lineno=37, end_col_offset=17, value='passlib', kind=None),
                                Constant(lineno=38, col_offset=8, end_lineno=38, end_col_offset=16, value='pillow', kind=None),
                                Constant(lineno=39, col_offset=8, end_lineno=39, end_col_offset=15, value='polib', kind=None),
                                Constant(lineno=40, col_offset=8, end_lineno=40, end_col_offset=16, value='psutil', kind=None),
                                Constant(lineno=41, col_offset=8, end_lineno=41, end_col_offset=25, value='psycopg2 >= 2.2', kind=None),
                                Constant(lineno=42, col_offset=8, end_lineno=42, end_col_offset=15, value='pydot', kind=None),
                                Constant(lineno=43, col_offset=8, end_lineno=43, end_col_offset=19, value='pyopenssl', kind=None),
                                Constant(lineno=44, col_offset=8, end_lineno=44, end_col_offset=16, value='pypdf2', kind=None),
                                Constant(lineno=45, col_offset=8, end_lineno=45, end_col_offset=18, value='pyserial', kind=None),
                                Constant(lineno=46, col_offset=8, end_lineno=46, end_col_offset=25, value='python-dateutil', kind=None),
                                Constant(lineno=47, col_offset=8, end_lineno=47, end_col_offset=23, value='python-stdnum', kind=None),
                                Constant(lineno=48, col_offset=8, end_lineno=48, end_col_offset=14, value='pytz', kind=None),
                                Constant(lineno=49, col_offset=8, end_lineno=49, end_col_offset=26, value='pyusb >= 1.0.0b1', kind=None),
                                Constant(lineno=50, col_offset=8, end_lineno=50, end_col_offset=16, value='qrcode', kind=None),
                                Constant(lineno=51, col_offset=8, end_lineno=51, end_col_offset=19, value='reportlab', kind=None),
                                Constant(lineno=52, col_offset=8, end_lineno=52, end_col_offset=18, value='requests', kind=None),
                                Constant(lineno=53, col_offset=8, end_lineno=53, end_col_offset=14, value='zeep', kind=None),
                                Constant(lineno=54, col_offset=8, end_lineno=54, end_col_offset=17, value='vobject', kind=None),
                                Constant(lineno=55, col_offset=8, end_lineno=55, end_col_offset=18, value='werkzeug', kind=None),
                                Constant(lineno=56, col_offset=8, end_lineno=56, end_col_offset=20, value='xlsxwriter', kind=None),
                                Constant(lineno=57, col_offset=8, end_lineno=57, end_col_offset=14, value='xlwt', kind=None),
                            ],
                            ctx=Load(),
                        ),
                    ),
                    keyword(
                        lineno=59,
                        col_offset=4,
                        end_lineno=59,
                        end_col_offset=27,
                        arg='python_requires',
                        value=Constant(lineno=59, col_offset=20, end_lineno=59, end_col_offset=27, value='>=3.7', kind=None),
                    ),
                    keyword(
                        lineno=60,
                        col_offset=4,
                        end_lineno=63,
                        end_col_offset=5,
                        arg='extras_require',
                        value=Dict(
                            lineno=60,
                            col_offset=19,
                            end_lineno=63,
                            end_col_offset=5,
                            keys=[
                                Constant(lineno=61, col_offset=8, end_lineno=61, end_col_offset=14, value='ldap', kind=None),
                                Constant(lineno=62, col_offset=8, end_lineno=62, end_col_offset=13, value='SSL', kind=None),
                            ],
                            values=[
                                List(
                                    lineno=61,
                                    col_offset=16,
                                    end_lineno=61,
                                    end_col_offset=31,
                                    elts=[Constant(lineno=61, col_offset=17, end_lineno=61, end_col_offset=30, value='python-ldap', kind=None)],
                                    ctx=Load(),
                                ),
                                List(
                                    lineno=62,
                                    col_offset=15,
                                    end_lineno=62,
                                    end_col_offset=28,
                                    elts=[Constant(lineno=62, col_offset=16, end_lineno=62, end_col_offset=27, value='pyopenssl', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                        ),
                    ),
                    keyword(
                        lineno=64,
                        col_offset=4,
                        end_lineno=66,
                        end_col_offset=5,
                        arg='tests_require',
                        value=List(
                            lineno=64,
                            col_offset=18,
                            end_lineno=66,
                            end_col_offset=5,
                            elts=[Constant(lineno=65, col_offset=8, end_lineno=65, end_col_offset=19, value='freezegun', kind=None)],
                            ctx=Load(),
                        ),
                    ),
                ],
            ),
        ),
    ],
    type_ignores=[],
)