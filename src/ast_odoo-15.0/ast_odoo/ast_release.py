Module(
    body=[
        Assign(
            targets=[
                Name(id='RELEASE_LEVELS', ctx=Store()),
                List(
                    elts=[
                        Name(id='ALPHA', ctx=Store()),
                        Name(id='BETA', ctx=Store()),
                        Name(id='RELEASE_CANDIDATE', ctx=Store()),
                        Name(id='FINAL', ctx=Store()),
                    ],
                    ctx=Store(),
                ),
            ],
            value=List(
                elts=[
                    Constant(value='alpha', kind=None),
                    Constant(value='beta', kind=None),
                    Constant(value='candidate', kind=None),
                    Constant(value='final', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='RELEASE_LEVELS_DISPLAY', ctx=Store())],
            value=Dict(
                keys=[
                    Name(id='ALPHA', ctx=Load()),
                    Name(id='BETA', ctx=Load()),
                    Name(id='RELEASE_CANDIDATE', ctx=Load()),
                    Name(id='FINAL', ctx=Load()),
                ],
                values=[
                    Name(id='ALPHA', ctx=Load()),
                    Name(id='BETA', ctx=Load()),
                    Constant(value='rc', kind=None),
                    Constant(value='', kind=None),
                ],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='version_info', ctx=Store())],
            value=Tuple(
                elts=[
                    Constant(value=15, kind=None),
                    Constant(value=0, kind=None),
                    Constant(value=0, kind=None),
                    Name(id='FINAL', ctx=Load()),
                    Constant(value=0, kind=None),
                    Constant(value='', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='version', ctx=Store())],
            value=BinOp(
                left=BinOp(
                    left=BinOp(
                        left=Call(
                            func=Attribute(
                                value=Constant(value='.', kind=None),
                                attr='join',
                                ctx=Load(),
                            ),
                            args=[
                                GeneratorExp(
                                    elt=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[Name(id='s', ctx=Load())],
                                        keywords=[],
                                    ),
                                    generators=[
                                        comprehension(
                                            target=Name(id='s', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='version_info', ctx=Load()),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=2, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                            ifs=[],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ],
                            keywords=[],
                        ),
                        op=Add(),
                        right=Subscript(
                            value=Name(id='RELEASE_LEVELS_DISPLAY', ctx=Load()),
                            slice=Subscript(
                                value=Name(id='version_info', ctx=Load()),
                                slice=Constant(value=3, kind=None),
                                ctx=Load(),
                            ),
                            ctx=Load(),
                        ),
                    ),
                    op=Add(),
                    right=Call(
                        func=Name(id='str', ctx=Load()),
                        args=[
                            BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Name(id='version_info', ctx=Load()),
                                        slice=Constant(value=4, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                ),
                op=Add(),
                right=Subscript(
                    value=Name(id='version_info', ctx=Load()),
                    slice=Constant(value=5, kind=None),
                    ctx=Load(),
                ),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Name(id='series', ctx=Store()),
                Name(id='serie', ctx=Store()),
                Name(id='major_version', ctx=Store()),
            ],
            value=Call(
                func=Attribute(
                    value=Constant(value='.', kind=None),
                    attr='join',
                    ctx=Load(),
                ),
                args=[
                    GeneratorExp(
                        elt=Call(
                            func=Name(id='str', ctx=Load()),
                            args=[Name(id='s', ctx=Load())],
                            keywords=[],
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='s', ctx=Store()),
                                iter=Subscript(
                                    value=Name(id='version_info', ctx=Load()),
                                    slice=Slice(
                                        lower=None,
                                        upper=Constant(value=2, kind=None),
                                        step=None,
                                    ),
                                    ctx=Load(),
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='product_name', ctx=Store())],
            value=Constant(value='Odoo', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='description', ctx=Store())],
            value=Constant(value='Odoo Server', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='long_desc', ctx=Store())],
            value=Constant(value='Odoo is a complete ERP and CRM. The main features are accounting (analytic\nand financial), stock management, sales and purchases management, tasks\nautomation, marketing campaigns, help desk, POS, etc. Technical features include\na distributed server, an object database, a dynamic GUI,\ncustomizable reports, and XML-RPC interfaces.\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='classifiers', ctx=Store())],
            value=Constant(value='Development Status :: 5 - Production/Stable\nLicense :: OSI Approved :: GNU Lesser General Public License v3\n\nProgramming Language :: Python\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='url', ctx=Store())],
            value=Constant(value='https://www.odoo.com', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='author', ctx=Store())],
            value=Constant(value='OpenERP S.A.', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='author_email', ctx=Store())],
            value=Constant(value='info@odoo.com', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='license', ctx=Store())],
            value=Constant(value='LGPL-3', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='nt_service_name', ctx=Store())],
            value=BinOp(
                left=Constant(value='odoo-server-', kind=None),
                op=Add(),
                right=Call(
                    func=Attribute(
                        value=Name(id='series', ctx=Load()),
                        attr='replace',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='~', kind=None),
                        Constant(value='-', kind=None),
                    ],
                    keywords=[],
                ),
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
