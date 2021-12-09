Module(
    body=[
        Import(
            names=[alias(name='hashlib', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.urls',
            names=[alias(name='url_quote', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname='M')],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='html_escape', asname='escape')],
            level=0,
        ),
        ClassDef(
            name='Image',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    Widget options:\n\n    ``class``\n        set as attribute on the generated <img> tag\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_src_urls',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Considering the rendering options, returns the src and data-zoom-image urls.\n\n        :return: src, src_zoom urls\n        :rtype: tuple\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='max_size', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='resize', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='max_size', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='resize', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='max_width', ctx=Store()),
                                                Name(id='max_height', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='max_width', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='options', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='max_height', kind=None),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='max_width', ctx=Load()),
                                            Name(id='max_height', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='max_size', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='%sx%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='max_width', ctx=Load()),
                                                        Name(id='max_height', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='sha', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='hashlib', ctx=Load()),
                                                attr='sha512',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[
                                                                Call(
                                                                    func=Name(id='getattr', ctx=Load()),
                                                                    args=[
                                                                        Name(id='record', ctx=Load()),
                                                                        Constant(value='__last_update', kind=None),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        attr='encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='utf-8', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='hexdigest',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Constant(value=7, kind=None),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='max_size', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='max_size', ctx=Load()),
                                    ops=[Is()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Constant(value='', kind=None),
                                orelse=BinOp(
                                    left=Constant(value='/%s', kind=None),
                                    op=Mod(),
                                    right=Name(id='max_size', ctx=Load()),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='filename-field', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='filename-field', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Subscript(
                                            value=Name(id='options', ctx=Load()),
                                            slice=Constant(value='filename-field', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='filename', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='filename', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='filename', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='filename', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='filename', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='filename', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='/', kind=None),
                                                    Constant(value='-', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='replace',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='\\', kind=None),
                                            Constant(value='-', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='..', kind=None),
                                    Constant(value='--', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='src', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='/web/image/%s/%s/%s%s/%s?unique=%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_name',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='options', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='preview_image', kind=None),
                                                Name(id='field_name', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        Name(id='max_size', ctx=Load()),
                                        Call(
                                            func=Name(id='url_quote', ctx=Load()),
                                            args=[Name(id='filename', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Name(id='sha', ctx=Load()),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='src_zoom', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='zoom', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='zoom', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='src_zoom', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/web/image/%s/%s/%s%s/%s?unique=%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='record', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='zoom', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='max_size', ctx=Load()),
                                                Call(
                                                    func=Name(id='url_quote', ctx=Load()),
                                                    args=[Name(id='filename', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                Name(id='sha', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='zoom', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='src_zoom', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='zoom', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='src', ctx=Load()),
                                    Name(id='src_zoom', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='record_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='options', ctx=Load()),
                                    slice=Constant(value='tagName', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='img', kind=None)],
                            ),
                            msg=Constant(value='Oddly enough, the root tag of an image field can not be img. That is because the image goes into the tag, or it gets the hose again.', kind=None),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='qweb_img_raw_data', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Image', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='record_to_html',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Name(id='field_name', ctx=Load()),
                                            Name(id='options', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='aclasses', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='qweb_img_responsive', kind=None),
                                        Constant(value=True, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                body=List(
                                    elts=[
                                        Constant(value='img', kind=None),
                                        Constant(value='img-fluid', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=List(
                                    elts=[Constant(value='img', kind=None)],
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='aclasses', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='class', kind=None),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='classes', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value=' ', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Name(id='escape', ctx=Load()),
                                            Name(id='aclasses', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='src', ctx=Store()),
                                        Name(id='src_zoom', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_src_urls',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='record', ctx=Load()),
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='options', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='alt-field', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='record', ctx=Load()),
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='alt-field', kind=None),
                                                ctx=Load(),
                                            ),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='alt', ctx=Store())],
                                    value=Call(
                                        func=Name(id='escape', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Subscript(
                                                    value=Name(id='options', ctx=Load()),
                                                    slice=Constant(value='alt-field', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='alt', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='alt', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='alt', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='alt', ctx=Store())],
                                            value=Call(
                                                func=Name(id='escape', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='display_name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='itemprop', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='itemprop', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='itemprop', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='options', ctx=Load()),
                                        slice=Constant(value='itemprop', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='atts', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedDict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='src', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='src', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='itemprop', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='itemprop', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='class', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='classes', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='style', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='style', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='alt', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='alt', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='data-zoom', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='src_zoom', ctx=Load()),
                                            Constant(value='1', kind='u'),
                                        ],
                                    ),
                                    Constant(value=None, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='data-zoom-image', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='src_zoom', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='atts', ctx=Load()),
                                    slice=Constant(value='data-no-post-process', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='options', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data-no-post-process', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='atts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.qweb', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_post_processing_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='img', kind=None),
                                    Name(id='atts', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='template_options', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='img', ctx=Store())],
                            value=List(
                                elts=[Constant(value='<img', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='name', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='atts', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='value', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value=' ', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='escape', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='pycompat', ctx=Load()),
                                                                    attr='to_text',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='name', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='="', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='escape', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='pycompat', ctx=Load()),
                                                                    attr='to_text',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='img', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='"', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='img', ctx=Load()),
                                    attr='append',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/>', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='M', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Constant(value='', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='img', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='ImageUrlConverter',
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
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Qweb Field Image', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb.field.image_url', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_src_urls',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='image_url', ctx=Store())],
                            value=Subscript(
                                value=Name(id='record', ctx=Load()),
                                slice=Call(
                                    func=Attribute(
                                        value=Name(id='options', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='preview_image', kind=None),
                                        Name(id='field_name', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='image_url', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='zoom', kind=None),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                ctx=Load(),
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
