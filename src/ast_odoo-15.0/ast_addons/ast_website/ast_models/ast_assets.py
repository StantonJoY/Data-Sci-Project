Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ClassDef(
            name='Assets',
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
                    value=Constant(value='web_editor.assets', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='make_scss_customization',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Makes a scss customization of the given file. That file must\n        contain a scss map including a line comment containing the word 'hook',\n        to indicate the location where to write the new key,value pairs.\n\n        Params:\n            url (str):\n                the URL of the scss file to customize (supposed to be a variable\n                file which will appear in the assets_common bundle)\n\n            values (dict):\n                key,value mapping to integrate in the file's map (containing the\n                word hook). If a key is already in the file's map, its value is\n                overridden.\n        ", kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='color-palettes-name', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='reset_asset',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/website/static/src/scss/options/colors/user_color_palette.scss', kind=None),
                                            Constant(value='web.assets_common', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='reset_asset',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/website/static/src/scss/options/colors/user_gray_color_palette.scss', kind=None),
                                            Constant(value='web.assets_common', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='make_scss_customization',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/website/static/src/scss/options/colors/user_theme_color_palette.scss', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='success', kind=None),
                                                    Constant(value='info', kind=None),
                                                    Constant(value='warning', kind=None),
                                                    Constant(value='danger', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='make_scss_customization',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/website/static/src/scss/options/user_values.scss', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='menu-gradient', kind=None),
                                                    Constant(value='header-boxed-gradient', kind=None),
                                                    Constant(value='footer-gradient', kind=None),
                                                    Constant(value='copyright-gradient', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                    Constant(value='null', kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='custom_url', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='make_custom_asset_file_url',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Constant(value='web.assets_common', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='updatedFileContent', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_asset_content',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='custom_url', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_asset_content',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='updatedFileContent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='updatedFileContent', ctx=Load()),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
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
                                    value=Name(id='values', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='pattern', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value="'%s': %%s,\n", kind=None),
                                        op=Mod(),
                                        right=Name(id='name', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='regex', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='compile',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='pattern', ctx=Load()),
                                                op=Mod(),
                                                right=Constant(value='.+', kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='replacement', ctx=Store())],
                                    value=BinOp(
                                        left=Name(id='pattern', ctx=Load()),
                                        op=Mod(),
                                        right=Name(id='value', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='regex', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='updatedFileContent', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='updatedFileContent', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='regex', ctx=Load()),
                                                    Name(id='replacement', ctx=Load()),
                                                    Name(id='updatedFileContent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='updatedFileContent', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='( *)(.*hook.*)', kind=None),
                                                    BinOp(
                                                        left=Constant(value='\\1%s\\1\\2', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='replacement', ctx=Load()),
                                                    ),
                                                    Name(id='updatedFileContent', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='save_asset',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='url', ctx=Load()),
                                    Constant(value='web.assets_common', kind=None),
                                    Name(id='updatedFileContent', ctx=Load()),
                                    Constant(value='scss', kind=None),
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
                    name='_get_custom_attachment',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='custom_url', annotation=None, type_comment=None),
                            arg(arg='op', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value='=', kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        See web_editor.Assets._get_custom_attachment\n        Extend to only return the attachments related to the current website.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Assets', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_custom_attachment',
                                    ctx=Load(),
                                ),
                                args=[Name(id='custom_url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='op',
                                        value=Name(id='op', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='website_id',
                                                value=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='x', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=Or(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='website_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='x', ctx=Load()),
                                                        attr='website_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Name(id='website', ctx=Load())],
                                                ),
                                            ],
                                        ),
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
                    name='_get_custom_asset',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='custom_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        See web_editor.Assets._get_custom_asset\n        Extend to only return the views related to the current website.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Assets', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_custom_asset',
                                    ctx=Load(),
                                ),
                                args=[Name(id='custom_url', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='website_id',
                                                value=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    attr='filter_duplicate',
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
                    name='_save_asset_hook',
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
                            value=Constant(value='\n        See web_editor.Assets._save_asset_hook\n        Extend to add website ID at attachment creation.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Assets', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_save_asset_hook',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='website', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get_current_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='website', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='website_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='website', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
