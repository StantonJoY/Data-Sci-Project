Module(
    body=[
        ImportFrom(
            module='base64',
            names=[alias(name='b64encode', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='hashlib',
            names=[alias(name='sha512', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
                alias(name='api', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='html_escape', asname=None),
                alias(name='file_open', asname=None),
            ],
            level=0,
        ),
        FunctionDef(
            name='get_hsl_from_seed',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='seed', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='hashed_seed', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Name(id='sha512', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='seed', ctx=Load()),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
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
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='hue', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='hashed_seed', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=0, kind=None),
                                            upper=Constant(value=2, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Constant(value=16, kind=None),
                                ],
                                keywords=[],
                            ),
                            op=Mult(),
                            right=Constant(value=360, kind=None),
                        ),
                        op=Div(),
                        right=Constant(value=255, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sat', ctx=Store())],
                    value=BinOp(
                        left=BinOp(
                            left=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Name(id='hashed_seed', ctx=Load()),
                                        slice=Slice(
                                            lower=Constant(value=2, kind=None),
                                            upper=Constant(value=4, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    Constant(value=16, kind=None),
                                ],
                                keywords=[],
                            ),
                            op=Mult(),
                            right=BinOp(
                                left=BinOp(
                                    left=Constant(value=70, kind=None),
                                    op=Sub(),
                                    right=Constant(value=40, kind=None),
                                ),
                                op=Div(),
                                right=Constant(value=255, kind=None),
                            ),
                        ),
                        op=Add(),
                        right=Constant(value=40, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='lig', ctx=Store())],
                    value=Constant(value=45, kind=None),
                    type_comment=None,
                ),
                Return(
                    value=JoinedStr(
                        values=[
                            Constant(value='hsl(', kind=None),
                            FormattedValue(
                                value=Name(id='hue', ctx=Load()),
                                conversion=-1,
                                format_spec=JoinedStr(
                                    values=[Constant(value='.0f', kind=None)],
                                ),
                            ),
                            Constant(value=', ', kind=None),
                            FormattedValue(
                                value=Name(id='sat', ctx=Load()),
                                conversion=-1,
                                format_spec=JoinedStr(
                                    values=[Constant(value='.0f', kind=None)],
                                ),
                            ),
                            Constant(value='%, ', kind=None),
                            FormattedValue(
                                value=Name(id='lig', ctx=Load()),
                                conversion=-1,
                                format_spec=JoinedStr(
                                    values=[Constant(value='.0f', kind=None)],
                                ),
                            ),
                            Constant(value='%)', kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='AvatarMixin',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='avatar.mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=List(
                        elts=[Constant(value='image.mixin', kind=None)],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Avatar Mixin', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_avatar_name_field', ctx=Store())],
                    value=Constant(value='name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='avatar_1920', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Avatar', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=1920, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=1920, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_avatar_1920', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='avatar_1024', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Avatar 1024', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=1024, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=1024, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_avatar_1024', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='avatar_512', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Avatar 512', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=512, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=512, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_avatar_512', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='avatar_256', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Avatar 256', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=256, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=256, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_avatar_256', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='avatar_128', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Image',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Avatar 128', kind=None)],
                        keywords=[
                            keyword(
                                arg='max_width',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='max_height',
                                value=Constant(value=128, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_avatar_128', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='avatar_field', annotation=None, type_comment=None),
                            arg(arg='image_field', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='avatar', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='image_field', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='avatar', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_avatar_name_field',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='avatar', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_avatar_generate_svg',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='avatar', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_avatar_get_placeholder',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='record', ctx=Load()),
                                            slice=Name(id='avatar_field', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='avatar', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar_1920',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_avatar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='avatar_1920', kind=None),
                                    Constant(value='image_1920', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='image_1920', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar_1024',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_avatar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='avatar_1024', kind=None),
                                    Constant(value='image_1024', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='image_1024', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar_512',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_avatar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='avatar_512', kind=None),
                                    Constant(value='image_512', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='image_512', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar_256',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_avatar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='avatar_256', kind=None),
                                    Constant(value='image_256', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='image_256', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_avatar_128',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_compute_avatar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='avatar_128', kind=None),
                                    Constant(value='image_128', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=List(
                                        elts=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            Constant(value='image_128', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_avatar_generate_svg',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='initial', ctx=Store())],
                            value=Call(
                                func=Name(id='html_escape', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='self', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_avatar_name_field',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='upper',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bgcolor', ctx=Store())],
                            value=Call(
                                func=Name(id='get_hsl_from_seed', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Subscript(
                                            value=Name(id='self', ctx=Load()),
                                            slice=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_avatar_name_field',
                                                ctx=Load(),
                                            ),
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                IfExp(
                                                    test=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='create_date',
                                                        ctx=Load(),
                                                    ),
                                                    body=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='create_date',
                                                                ctx=Load(),
                                                            ),
                                                            attr='timestamp',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    orelse=Constant(value='', kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='b64encode', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value="<?xml version='1.0' encoding='UTF-8' ?><svg height='180' width='180' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'><rect fill='", kind=None),
                                                    FormattedValue(
                                                        value=Name(id='bgcolor', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value="' height='180' width='180'/><text fill='#ffffff' font-size='96' text-anchor='middle' x='90' y='125' font-family='sans-serif'>", kind=None),
                                                    FormattedValue(
                                                        value=Name(id='initial', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='</text></svg>', kind=None),
                                                ],
                                            ),
                                            attr='encode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_avatar_get_placeholder_path',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Constant(value='base/static/img/avatar_grey.png', kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_avatar_get_placeholder',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='b64encode', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='file_open', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_avatar_get_placeholder_path',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
