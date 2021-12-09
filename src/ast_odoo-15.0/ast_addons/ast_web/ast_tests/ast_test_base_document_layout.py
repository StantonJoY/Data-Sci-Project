Module(
    body=[
        Import(
            names=[alias(name='os', asname=None)],
        ),
        ImportFrom(
            module='PIL',
            names=[alias(name='Image', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests',
            names=[
                alias(name='TransactionCase', asname=None),
                alias(name='tagged', asname=None),
                alias(name='Form', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='frozendict', asname=None),
                alias(name='image_to_base64', asname=None),
                alias(name='hex_to_rgb', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='dir_path', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Attribute(
                        value=Name(id='os', ctx=Load()),
                        attr='path',
                        ctx=Load(),
                    ),
                    attr='dirname',
                    ctx=Load(),
                ),
                args=[
                    Call(
                        func=Attribute(
                            value=Attribute(
                                value=Name(id='os', ctx=Load()),
                                attr='path',
                                ctx=Load(),
                            ),
                            attr='realpath',
                            ctx=Load(),
                        ),
                        args=[Name(id='__file__', ctx=Load())],
                        keywords=[],
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_file_cache', ctx=Store())],
            value=Dict(keys=[], values=[]),
            type_comment=None,
        ),
        ClassDef(
            name='TestBaseDocumentLayoutHelpers',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUp',
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='TestBaseDocumentLayoutHelpers', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUp',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='color_fields',
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Constant(value='primary_color', kind=None),
                                    Constant(value='secondary_color', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                attr='company',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='css_color_error',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_templates_and_layouts',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_images',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='assertColors',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='checked_obj', annotation=None, type_comment=None),
                            arg(arg='expected', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='_expected_getter', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='expected', ctx=Load()),
                                        Name(id='dict', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                body=Attribute(
                                    value=Name(id='expected', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                orelse=Call(
                                    func=Name(id='partial', ctx=Load()),
                                    args=[
                                        Name(id='getattr', ctx=Load()),
                                        Name(id='expected', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='color_fields',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='color1', ctx=Store())],
                                    value=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='checked_obj', ctx=Load()),
                                            Name(id='fname', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='color2', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_expected_getter', ctx=Load()),
                                        args=[Name(id='fname', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='css_color_error',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_compare_colors_rgb',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='color1', ctx=Load()),
                                                    Name(id='color2', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertEqual',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='color1', ctx=Load()),
                                                    Name(id='color2', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
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
                    name='_compare_colors_rgb',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='color1', annotation=None, type_comment=None),
                            arg(arg='color2', annotation=None, type_comment=None),
                        ],
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='color1', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[Name(id='color2', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='color1', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='color1', ctx=Store())],
                            value=Call(
                                func=Name(id='hex_to_rgb', ctx=Load()),
                                args=[Name(id='color1', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='color2', ctx=Store())],
                            value=Call(
                                func=Name(id='hex_to_rgb', ctx=Load()),
                                args=[Name(id='color2', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='color1', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='color2', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[Name(id='color1', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertAlmostEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='color1', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Subscript(
                                                value=Name(id='color2', ctx=Load()),
                                                slice=Name(id='i', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='delta',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='css_color_error',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
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
                    name='_get_images_for_test',
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
                            value=List(
                                elts=[
                                    Constant(value='sweden.png', kind=None),
                                    Constant(value='odoo.png', kind=None),
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
                    name='_set_images',
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
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_images_for_test',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='fname_split', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fname', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Compare(
                                            left=Subscript(
                                                value=Name(id='fname_split', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            ops=[In()],
                                            comparators=[Name(id='_file_cache', ctx=Load())],
                                        ),
                                    ),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='Image', ctx=Load()),
                                                            attr='open',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='os', ctx=Load()),
                                                                        attr='path',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='dir_path', ctx=Load()),
                                                                    Name(id='fname', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Constant(value='r', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    optional_vars=Name(id='img', ctx=Store()),
                                                ),
                                            ],
                                            body=[
                                                Assign(
                                                    targets=[Name(id='base64_img', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='image_to_base64', ctx=Load()),
                                                        args=[
                                                            Name(id='img', ctx=Load()),
                                                            Constant(value='PNG', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='primary', ctx=Store()),
                                                                Name(id='secondary', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='base.document.layout', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='extract_image_primary_secondary_colors',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='base64_img', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='_img', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='frozendict', ctx=Load()),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='img', kind=None),
                                                                    Constant(value='colors', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='base64_img', ctx=Load()),
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='primary_color', kind=None),
                                                                            Constant(value='secondary_color', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Name(id='primary', ctx=Load()),
                                                                            Name(id='secondary', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='_file_cache', ctx=Load()),
                                                            slice=Subscript(
                                                                value=Name(id='fname_split', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='_img', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_imgs',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='frozendict', ctx=Load()),
                                args=[Name(id='_file_cache', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_templates_and_layouts',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='layout_template1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='key', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='layout_template1', kind=None),
                                            Constant(value='web.layout_template1', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<div></div>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template1',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ir.ui.view', kind=None),
                                            Constant(value='web', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_colors',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='primary_color', kind=None),
                                    Constant(value='secondary_color', kind=None),
                                ],
                                values=[
                                    Constant(value='#000000', kind=None),
                                    Constant(value='#000000', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='report_layout1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.layout', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template1',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='report_%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='layout_template1',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='layout_template2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='key', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='arch', kind=None),
                                        ],
                                        values=[
                                            Constant(value='layout_template2', kind=None),
                                            Constant(value='web.layout_template2', kind=None),
                                            Constant(value='qweb', kind=None),
                                            Constant(value='<div></div>', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.data', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='model', kind=None),
                                            Constant(value='module', kind=None),
                                            Constant(value='res_id', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template2',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ir.ui.view', kind=None),
                                            Constant(value='web', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='report_layout2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='report.layout', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='view_id', kind=None),
                                            Constant(value='name', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='layout_template2',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='report_%s', kind=None),
                                                op=Mod(),
                                                right=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='layout_template2',
                                                        ctx=Load(),
                                                    ),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestBaseDocumentLayout',
            bases=[Name(id='TestBaseDocumentLayoutHelpers', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_company_no_color_change_logo',
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
                            value=Constant(value="When neither a logo nor the colors are set\n        The wizard displays the colors of the report layout\n        Changing logo means the colors on the wizard change too\n        Emptying the logo works and doesn't change the colors", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='external_report_layout_id', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='web.layout_template1', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='default_colors', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='default_colors',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Name(id='default_colors', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='doc_layout', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_imgs',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='sweden', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='img', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='doc_layout', ctx=Load()),
                                                attr='logo',
                                                ctx=Load(),
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_company_no_color_but_logo_change_logo',
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
                            value=Constant(value='When company colors are not set, but a logo is,\n        the wizard displays the computed colors from the logo', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#ff0080', kind=None),
                                            Constant(value='#00ff00', kind=None),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='img', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_imgs',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='odoo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='img', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='odoo', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_company_colors_change_logo',
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
                            value=Constant(value='changes of the logo implies displaying the new computed colors', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#ff0080', kind=None),
                                            Constant(value='#00ff00', kind=None),
                                            Constant(value=False, kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_imgs',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='odoo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='img', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='odoo', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_company_colors_and_logo_change_logo',
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
                            value=Constant(value="The colors of the company may differ from the one the logo computes\n        Opening the wizard in these condition displays the company's colors\n        When the logo changes, colors must change according to the logo", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#ff0080', kind=None),
                                            Constant(value='#00ff00', kind=None),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='img', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='logo',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_imgs',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='odoo', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='img', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='odoo', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_company_colors_reset_colors',
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
                            value=Constant(value='Reset the colors when they differ from the ones originally\n        computed from the company logo', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='logo', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#ff0080', kind=None),
                                            Constant(value='#00ff00', kind=None),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='img', kind=None),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='primary_color',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='doc_layout', ctx=Load()),
                                        attr='logo_primary_color',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='doc_layout', ctx=Load()),
                                            attr='secondary_color',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='doc_layout', ctx=Load()),
                                        attr='logo_secondary_color',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertColors',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='doc_layout', ctx=Load()),
                                            Subscript(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_imgs',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sweden', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='colors', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_parse_company_colors_grayscale',
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
                            value=Constant(value='Grayscale images with transparency - make sure the color extraction does not crash', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='primary_color', kind=None),
                                            Constant(value='secondary_color', kind=None),
                                            Constant(value='paperformat_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='#ff0080', kind=None),
                                            Constant(value='#00ff00', kind=None),
                                            Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ref',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='base.paperformat_us', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='Form', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='base.document.layout', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    optional_vars=Name(id='doc_layout', ctx=Store()),
                                ),
                            ],
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='Image', ctx=Load()),
                                                    attr='open',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='os', ctx=Load()),
                                                                attr='path',
                                                                ctx=Load(),
                                                            ),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='dir_path', ctx=Load()),
                                                            Constant(value='logo_ci.png', kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value='r', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='img', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='base64_img', ctx=Store())],
                                            value=Call(
                                                func=Name(id='image_to_base64', ctx=Load()),
                                                args=[
                                                    Name(id='img', ctx=Load()),
                                                    Constant(value='PNG', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='doc_layout', ctx=Load()),
                                                    attr='logo',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='base64_img', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=None, kind=None),
                                            Attribute(
                                                value=Name(id='doc_layout', ctx=Load()),
                                                attr='primary_color',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Name(id='tagged', ctx=Load()),
                    args=[Constant(value='document_layout', kind=None)],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
