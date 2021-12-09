Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Http',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='binary_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='id', annotation=None, type_comment=None),
                            arg(arg='field', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='filename', annotation=None, type_comment=None),
                            arg(arg='filename_field', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                            arg(arg='mimetype', annotation=None, type_comment=None),
                            arg(arg='default_mimetype', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='ir.attachment', kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='datas', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='name', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value='application/octet-stream', kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='obj', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='xmlid', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='obj', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_xmlid_to_obj',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            Name(id='xmlid', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='obj', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='slide.slide', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='obj', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='id', ctx=Load()),
                                            Compare(
                                                left=Name(id='model', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='slide.slide', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='obj', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Name(id='model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='int', ctx=Load()),
                                                        args=[Name(id='id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        If(
                            test=Name(id='obj', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='obj', ctx=Load()),
                                            attr='check_access_rights',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='obj', ctx=Load()),
                                            attr='check_access_rule',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='binary_content',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='xmlid',
                                        value=Name(id='xmlid', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='model',
                                        value=Name(id='model', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='id',
                                        value=Name(id='id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='field',
                                        value=Name(id='field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='unique',
                                        value=Name(id='unique', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename',
                                        value=Name(id='filename', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='filename_field',
                                        value=Name(id='filename_field', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='download',
                                        value=Name(id='download', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='mimetype',
                                        value=Name(id='mimetype', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='default_mimetype',
                                        value=Name(id='default_mimetype', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='access_token',
                                        value=Name(id='access_token', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
