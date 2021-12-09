Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='OrderedDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.assetsbundle',
            names=[alias(name='AssetsBundle', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='url_for', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.models',
            names=[alias(name='ir_http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='html_escape', asname='escape')],
            level=0,
        ),
        Assign(
            targets=[Name(id='re_background_image', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[Constant(value='(background-image\\s*:\\s*url\\(\\s*[\'\\"]?\\s*)([^)\'\\"]+)', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='AssetsBundleMultiWebsite',
            bases=[Name(id='AssetsBundle', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='_get_asset_url_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='id', annotation=None, type_comment=None),
                            arg(arg='unique', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='sep', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_id_path', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='%s/', kind=None),
                                                op=Mod(),
                                                right=Name(id='website_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra', ctx=Store())],
                            value=BinOp(
                                left=Name(id='website_id_path', ctx=Load()),
                                op=Add(),
                                right=Name(id='extra', ctx=Load()),
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
                                            Name(id='AssetsBundleMultiWebsite', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_asset_url_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='id', ctx=Load()),
                                    Name(id='unique', ctx=Load()),
                                    Name(id='extra', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='sep', ctx=Load()),
                                    Name(id='extension', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_assets_domain_for_already_processed_css',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='assets', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AssetsBundleMultiWebsite', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_assets_domain_for_already_processed_css',
                                    ctx=Load(),
                                ),
                                args=[Name(id='assets', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_website', ctx=Store())],
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
                                keywords=[
                                    keyword(
                                        arg='fallback',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='expression', ctx=Load()),
                                    attr='AND',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='res', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='current_website', ctx=Load()),
                                                    attr='website_domain',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_debug_asset_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='extra', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='extension', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value='%', kind=None),
                            Constant(value='%', kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_id_path', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website_id', ctx=Load()),
                                            BinOp(
                                                left=Constant(value='%s/', kind=None),
                                                op=Mod(),
                                                right=Name(id='website_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra', ctx=Store())],
                            value=BinOp(
                                left=Name(id='website_id_path', ctx=Load()),
                                op=Add(),
                                right=Name(id='extra', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='AssetsBundleMultiWebsite', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='get_debug_asset_url',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='extra', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Name(id='extension', ctx=Load()),
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
        ClassDef(
            name='QWeb',
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
                    value=Constant(value=' QWeb object for rendering stuff in the website context ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.qweb', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='URL_ATTRS', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='form', kind=None),
                            Constant(value='a', kind=None),
                            Constant(value='link', kind=None),
                            Constant(value='script', kind=None),
                            Constant(value='img', kind=None),
                        ],
                        values=[
                            Constant(value='action', kind=None),
                            Constant(value='href', kind=None),
                            Constant(value='href', kind=None),
                            Constant(value='src', kind=None),
                            Constant(value='src', kind=None),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_asset_bundle',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
                            arg(arg='files', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='css', annotation=None, type_comment=None),
                            arg(arg='js', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Name(id='AssetsBundleMultiWebsite', ctx=Load()),
                                args=[
                                    Name(id='xmlid', ctx=Load()),
                                    Name(id='files', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='env',
                                        value=Name(id='env', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_post_processing_att',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='tagName', annotation=None, type_comment=None),
                            arg(arg='atts', annotation=None, type_comment=None),
                            arg(arg='options', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='atts', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='data-no-post-process', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Name(id='atts', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='atts', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='QWeb', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_post_processing_att',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='tagName', ctx=Load()),
                                    Name(id='atts', ctx=Load()),
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
                                    Compare(
                                        left=Name(id='tagName', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='img', kind=None)],
                                    ),
                                    Compare(
                                        left=Constant(value='loading', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='atts', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='atts', ctx=Load()),
                                            slice=Constant(value='loading', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='lazy', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='inherit_branding', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rendering_bundle', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='edit_translations', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='debug', kind=None)],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='request', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='debug',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Name(id='atts', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ir_http', ctx=Load()),
                                    attr='get_request_website',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='website', ctx=Load()),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='options', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='options', ctx=Load()),
                                                slice=Constant(value='website_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='website', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='atts', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='name', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='URL_ATTRS',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='tagName', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Name(id='name', ctx=Load()),
                                    Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='atts', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='atts', ctx=Load()),
                                            slice=Name(id='name', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='url_for', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='atts', ctx=Load()),
                                                slice=Name(id='name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='cdn_activated',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Name(id='atts', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='data_name', ctx=Store())],
                            value=JoinedStr(
                                values=[
                                    Constant(value='data-', kind=None),
                                    FormattedValue(
                                        value=Name(id='name', ctx=Load()),
                                        conversion=-1,
                                        format_spec=None,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='name', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='atts', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='data_name', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='atts', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='atts', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OrderedDict', ctx=Load()),
                                        args=[Name(id='atts', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='atts', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='atts', ctx=Load()),
                                                    slice=Name(id='name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='get_cdn_url',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='atts', ctx=Load()),
                                                        slice=Name(id='name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='data_name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='atts', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='atts', ctx=Load()),
                                                    slice=Name(id='data_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='get_cdn_url',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='atts', ctx=Load()),
                                                        slice=Name(id='data_name', ctx=Load()),
                                                        ctx=Load(),
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='atts', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='style', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='str', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Constant(value='background-image', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='atts', ctx=Load()),
                                                slice=Constant(value='style', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='atts', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OrderedDict', ctx=Load()),
                                        args=[Name(id='atts', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                            value=Name(id='re_background_image', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='m', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BinOp(
                                                    left=Constant(value='%s%s', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='m', ctx=Load()),
                                                                    attr='group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=1, kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='website', ctx=Load()),
                                                                    attr='get_cdn_url',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='m', ctx=Load()),
                                                                            attr='group',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value=2, kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='atts', ctx=Load()),
                                                slice=Constant(value='style', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='atts', ctx=Load()),
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
