Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='os', asname=None)],
        ),
        Import(
            names=[alias(name='unittest', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.routing', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug.utils', asname=None)],
        ),
        ImportFrom(
            module='functools',
            names=[alias(name='partial', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
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
            module='odoo',
            names=[
                alias(name='registry', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='AccessError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[alias(name='safe_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[alias(name='FALSE_DOMAIN', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models',
            names=[alias(name='ir_http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='_guess_mimetype', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.portal.controllers.portal',
            names=[alias(name='_build_url_w_params', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='sitemap_qs2dom',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='qs', annotation=None, type_comment=None),
                    arg(arg='route', annotation=None, type_comment=None),
                    arg(arg='field', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='name', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=' Convert a query_string (can contains a path) to a domain', kind=None),
                ),
                Assign(
                    targets=[Name(id='dom', ctx=Store())],
                    value=List(elts=[], ctx=Load()),
                    type_comment=None,
                ),
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Name(id='qs', ctx=Load()),
                            Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='qs', ctx=Load()),
                                        attr='lower',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                ops=[NotIn()],
                                comparators=[Name(id='route', ctx=Load())],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='needles', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='qs', ctx=Load()),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='split',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='unittest', ctx=Load()),
                                        attr='util',
                                        ctx=Load(),
                                    ),
                                    attr='unorderable_list_difference',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='route', ctx=Load()),
                                                    attr='strip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='needles', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[Name(id='needles', ctx=Load())],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='dom', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Name(id='field', ctx=Load()),
                                                    Constant(value='ilike', kind=None),
                                                    Subscript(
                                                        value=Name(id='needles', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='dom', ctx=Store())],
                                    value=Name(id='FALSE_DOMAIN', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Name(id='dom', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='get_request_website',
            args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
            body=[
                Expr(
                    value=Constant(value=" Return the website set on `request` if called in a frontend context\n    (website=True on route).\n    This method can typically be used to check if we are in the frontend.\n\n    This method is easy to mock during python tests to simulate frontend\n    context, rather than mocking every method accessing request.website.\n\n    Don't import directly the method or it won't be mocked during tests, do:\n    ```\n    from odoo.addons.website.models import ir_http\n    my_var = ir_http.get_request_website()\n    ```\n    ", kind=None),
                ),
                Return(
                    value=BoolOp(
                        op=Or(),
                        values=[
                            BoolOp(
                                op=And(),
                                values=[
                                    Name(id='request', ctx=Load()),
                                    Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='request', ctx=Load()),
                                            Constant(value='website', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Constant(value=False, kind=None),
                        ],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
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
                    name='routing_map',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='key', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='request', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website_routing',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='routing_map',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Name(id='key', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='clear_caches',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
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
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_clear_routing_map',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='clear_caches',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_slug_matching',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='adapter', annotation=None, type_comment=None),
                            arg(arg='endpoint', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Name(id='arg', ctx=Store()),
                            iter=Name(id='kw', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='kw', ctx=Load()),
                                                slice=Name(id='arg', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='models', ctx=Load()),
                                                attr='BaseModel',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='kw', ctx=Load()),
                                                    slice=Name(id='arg', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='kw', ctx=Load()),
                                                        slice=Name(id='arg', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='slug_matching',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
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
                            targets=[Name(id='qs', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='query_string',
                                        ctx=Load(),
                                    ),
                                    attr='decode',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='utf-8', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='adapter', ctx=Load()),
                                        attr='build',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Name(id='endpoint', ctx=Load()),
                                        Name(id='kw', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=BoolOp(
                                    op=Or(),
                                    values=[
                                        BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='qs', ctx=Load()),
                                                BinOp(
                                                    left=Constant(value='?%s', kind=None),
                                                    op=Mod(),
                                                    right=Name(id='qs', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        Constant(value='', kind=None),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_match',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='path_info', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='key', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='key', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='request', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website_routing',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_match',
                                    ctx=Load(),
                                ),
                                args=[Name(id='path_info', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Name(id='key', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_generate_routing_rules',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='modules', annotation=None, type_comment=None),
                            arg(arg='converters', annotation=None, type_comment=None),
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
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='website_routing',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='logger', ctx=Load()),
                                    attr='debug',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='_generate_routing_rules for website: %s', kind=None),
                                    Name(id='website_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='redirect_type', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='308', kind=None),
                                                    Constant(value='404', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='website_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='website_id', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rewrites', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='x', ctx=Load()),
                                                    attr='url_from',
                                                    ctx=Load(),
                                                ),
                                                Name(id='x', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='x', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='request', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='website.rewrite', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='search',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='domain', ctx=Load())],
                                                    keywords=[],
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
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='cls', ctx=Load()),
                                        attr='_rewrite_len',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='website_id', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='rewrites', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='url', ctx=Store()),
                                    Name(id='endpoint', ctx=Store()),
                                    Name(id='routing', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_generate_routing_rules',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='modules', ctx=Load()),
                                    Name(id='converters', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='routing', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='routing', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='url', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='rewrites', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rewrite', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='rewrites', ctx=Load()),
                                                slice=Name(id='url', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='url_to', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='rewrite', ctx=Load()),
                                                attr='url_to',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='rewrite', ctx=Load()),
                                                    attr='redirect_type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='308', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='logger', ctx=Load()),
                                                            attr='debug',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Constant(value='Add rule %s for %s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Name(id='url_to', ctx=Load()),
                                                                        Name(id='website_id', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Yield(
                                                        value=Tuple(
                                                            elts=[
                                                                Name(id='url_to', ctx=Load()),
                                                                Name(id='endpoint', ctx=Load()),
                                                                Name(id='routing', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='url', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='url_to', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logger', ctx=Load()),
                                                                    attr='debug',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='Redirect from %s to %s for website %s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Name(id='url', ctx=Load()),
                                                                                Name(id='url_to', ctx=Load()),
                                                                                Name(id='website_id', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='_slug_matching', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='partial', ctx=Load()),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='cls', ctx=Load()),
                                                                        attr='_slug_matching',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='endpoint',
                                                                        value=Name(id='endpoint', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='routing', ctx=Load()),
                                                                    slice=Constant(value='redirect_to', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='_slug_matching', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Yield(
                                                                value=Tuple(
                                                                    elts=[
                                                                        Name(id='url', ctx=Load()),
                                                                        Name(id='endpoint', ctx=Load()),
                                                                        Name(id='routing', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='rewrite', ctx=Load()),
                                                            attr='redirect_type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='404', kind=None)],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='logger', ctx=Load()),
                                                                    attr='debug',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    BinOp(
                                                                        left=Constant(value='Return 404 for %s for website %s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Name(id='url', ctx=Load()),
                                                                                Name(id='website_id', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Continue(),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Yield(
                                                value=Tuple(
                                                    elts=[
                                                        Name(id='url', ctx=Load()),
                                                        Name(id='endpoint', ctx=Load()),
                                                        Name(id='routing', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_converters',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Get the converters list for custom url pattern werkzeug need to\n            match Rule. This override adds the website ones.\n        ', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Http', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_get_converters',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='model',
                                        value=Name(id='ModelConverter', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_auth_method_public',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' If no user logged, set the public user of current website, or default\n            public user as request uid.\n            After this method `request.env` can be called, since the `request.uid` is\n            set. The `env` lazy property of `request` will be correct.\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='env', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='api', ctx=Load()),
                                            attr='Environment',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='cr',
                                                ctx=Load(),
                                            ),
                                            Name(id='SUPERUSER_ID', ctx=Load()),
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='website', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='env', ctx=Load()),
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='uid',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='website', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='website', ctx=Load()),
                                                    attr='_get_cached',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='user_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                                    value=Name(id='request', ctx=Load()),
                                    attr='uid',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='Http', ctx=Load()),
                                                    Name(id='cls', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_auth_method_public',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_register_website_track',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='response', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='getattr', ctx=Load()),
                                    args=[
                                        Name(id='response', ctx=Load()),
                                        Constant(value='status_code', kind=None),
                                        Constant(value=0, kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=200, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='response', ctx=Load()),
                                    Constant(value='_cached_page', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='website_page', ctx=Store()),
                                                Name(id='template', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='_cached_page',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='_cached_template',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Constant(value='qcontext', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='main_object', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='response', ctx=Load()),
                                                        attr='qcontext',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='main_object', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='website_page', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Name(id='main_object', ctx=Load()),
                                                                Constant(value='_name', kind=None),
                                                                Constant(value=False, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='website.page', kind=None)],
                                                    ),
                                                    Name(id='main_object', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='template', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='response', ctx=Load()),
                                                        attr='qcontext',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='response_template', kind=None)],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='template', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get_template',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='template', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='view', ctx=Load()),
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='track',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.visitor', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_handle_webpage_dispatch',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='response', ctx=Load()),
                                            Name(id='website_page', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_postprocess_args',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='arguments', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='processing', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_postprocess_args',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='arguments', ctx=Load()),
                                    Name(id='rule', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='processing', ctx=Load()),
                            body=[
                                Return(
                                    value=Name(id='processing', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='arguments', ctx=Load()),
                                    attr='values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='record', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='models', ctx=Load()),
                                                        attr='BaseModel',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='record', ctx=Load()),
                                                    Constant(value='can_access_from_current_website', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='can_access_from_current_website',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.http', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_handle_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                                attr='exceptions',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='NotFound',
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
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='AccessError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        Return(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='request', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='ir.http', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_handle_exception',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='werkzeug', ctx=Load()),
                                                                                attr='exceptions',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='Forbidden',
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
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_dispatch',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        In case of rerouting for translate (e.g. when visiting odoo.com/fr_BE/),\n        _dispatch calls reroute() that returns _dispatch with altered request properties.\n        The second _dispatch will continue until end of process. When second _dispatch is finished, the first _dispatch\n        call receive the new altered request and continue.\n        At the end, 2 calls of _dispatch (and this override) are made with exact same request properties, instead of one.\n        As the response has not been sent back to the client, the visitor cookie does not exist yet when second _dispatch call\n        is treated in _handle_webpage_dispatch, leading to create 2 visitors with exact same properties.\n        To avoid this, we check if, !!! before calling super !!!, we are in a rerouting request. If not, it means that we are\n        handling the original request, in which we should create the visitor. We ignore every other rerouting requests.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='is_rerouting', ctx=Store())],
                            value=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='request', ctx=Load()),
                                    Constant(value='routing_iteration', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='session',
                                    ctx=Load(),
                                ),
                                attr='db',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='reg', ctx=Store())],
                                    value=Call(
                                        func=Name(id='registry', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='db',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Name(id='reg', ctx=Load()),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=Name(id='cr', ctx=Store()),
                                        ),
                                    ],
                                    body=[
                                        Assign(
                                            targets=[Name(id='env', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='api', ctx=Load()),
                                                    attr='Environment',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cr', ctx=Load()),
                                                    Name(id='SUPERUSER_ID', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='website_routing',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='env', ctx=Load()),
                                                            slice=Constant(value='website', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_current_website',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_dispatch',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='is_rerouting', ctx=Load()),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='_register_website_track',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='response', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_dispatch_parameters',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='func', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='force_website_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='args',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='fw', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='force_website_id', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='session',
                                                    ctx=Load(),
                                                ),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='force_website_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='force_website_id', ctx=Load())],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website.group_multi_website', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='has_group',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='website.group_website_publisher', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_force_website',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='httprequest',
                                                            ctx=Load(),
                                                        ),
                                                        attr='args',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='fw', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='context',
                                            ctx=Load(),
                                        ),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='tz', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='context', ctx=Load()),
                                            slice=Constant(value='tz', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='geoip', kind=None),
                                                    Dict(keys=[], values=[]),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='time_zone', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pytz', ctx=Load()),
                                                    attr='timezone',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='context', ctx=Load()),
                                                                slice=Constant(value='tz', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='', kind=None),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='UnknownTimeZoneError',
                                                ctx=Load(),
                                            ),
                                            name=None,
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='context', ctx=Load()),
                                                            attr='pop',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='tz', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='website',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
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
                            targets=[
                                Subscript(
                                    value=Name(id='context', ctx=Load()),
                                    slice=Constant(value='website_id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='website',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='website_company_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='_get_cached',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='company_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='website_company_id', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='company_ids',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='context', ctx=Load()),
                                            slice=Constant(value='allowed_company_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=List(
                                        elts=[Name(id='website_company_id', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='context', ctx=Load()),
                                            slice=Constant(value='allowed_company_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='company_id',
                                            ctx=Load(),
                                        ),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='context',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='context', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_add_dispatch_parameters',
                                    ctx=Load(),
                                ),
                                args=[Name(id='func', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='routing_iteration',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='context',
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
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_frontend_langs',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='get_request_website', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=ListComp(
                                        elt=Name(id='code', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='code', ctx=Store()),
                                                        Starred(
                                                            value=Name(id='_', ctx=Store()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.lang', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='get_available',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_get_frontend_langs',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_default_lang',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Name(id='getattr', ctx=Load()),
                                args=[
                                    Name(id='request', ctx=Load()),
                                    Constant(value='website', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.lang', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='website',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_cached',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='default_lang_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
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
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_default_lang',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_translation_frontend_modules_name',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='mods', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_translation_frontend_modules_name',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='installed', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='_init_modules',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Call(
                                    func=Name(id='set', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='conf',
                                                ctx=Load(),
                                            ),
                                            attr='server_wide_modules',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Name(id='mods', ctx=Load()),
                                op=Add(),
                                right=ListComp(
                                    elt=Name(id='mod', ctx=Load()),
                                    generators=[
                                        comprehension(
                                            target=Name(id='mod', ctx=Store()),
                                            iter=Name(id='installed', ctx=Load()),
                                            ifs=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='mod', ctx=Load()),
                                                        attr='startswith',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='website', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            is_async=0,
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_serve_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='req_page', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='path',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page_domain', ctx=Store())],
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='url', kind=None),
                                                Constant(value='=', kind=None),
                                                Name(id='req_page', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='website_domain',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='published_domain', ctx=Store())],
                            value=Name(id='page_domain', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.page', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='published_domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Constant(value='website_id asc', kind=None),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='page', ctx=Load()),
                                    ),
                                    Compare(
                                        left=Name(id='req_page', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='/', kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='req_page', ctx=Load()),
                                            attr='endswith',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='/', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='path', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=None,
                                            upper=UnaryOp(
                                                op=USub(),
                                                operand=Constant(value=1, kind=None),
                                            ),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='lang',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='_get_default_lang',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='path', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Constant(value='/', kind=None),
                                                    op=Add(),
                                                    right=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                        attr='url_code',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Name(id='path', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='query_string',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Name(id='path', ctx=Store()),
                                            op=Add(),
                                            value=BinOp(
                                                left=Constant(value='?', kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='httprequest',
                                                                ctx=Load(),
                                                            ),
                                                            attr='query_string',
                                                            ctx=Load(),
                                                        ),
                                                        attr='decode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='utf-8', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='path', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='code',
                                                value=Constant(value=301, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='page', ctx=Load()),
                            body=[
                                Expr(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='menu_id',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='page', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='website',
                                                        ctx=Load(),
                                                    ),
                                                    attr='is_publisher',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='is_visible',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='need_to_cache', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='cache_key', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='page', ctx=Load()),
                                            attr='_get_cache_key',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='request', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='page', ctx=Load()),
                                                attr='cache_time',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='httprequest',
                                                        ctx=Load(),
                                                    ),
                                                    attr='method',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='GET', kind=None)],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_is_public',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Constant(value='nocache', kind=None),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='params',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='session',
                                                        ctx=Load(),
                                                    ),
                                                    attr='debug',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='cache_key', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='cache_key', ctx=Load()),
                                                    slice=UnaryOp(
                                                        op=USub(),
                                                        operand=Constant(value=1, kind=None),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                ops=[IsNot()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='need_to_cache', ctx=Store())],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Try(
                                            body=[
                                                Assign(
                                                    targets=[Name(id='r', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='page', ctx=Load()),
                                                            attr='_get_cache_response',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='cache_key', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=BinOp(
                                                            left=Subscript(
                                                                value=Name(id='r', ctx=Load()),
                                                                slice=Constant(value='time', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            op=Add(),
                                                            right=Attribute(
                                                                value=Name(id='page', ctx=Load()),
                                                                attr='cache_time',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='time',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='response', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='odoo', ctx=Load()),
                                                                        attr='http',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='Response',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='r', ctx=Load()),
                                                                        slice=Constant(value='content', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='mimetype',
                                                                        value=Subscript(
                                                                            value=Name(id='r', ctx=Load()),
                                                                            slice=Constant(value='contenttype', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='response', ctx=Load()),
                                                                    attr='_cached_template',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Subscript(
                                                                value=Name(id='r', ctx=Load()),
                                                                slice=Constant(value='template', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='response', ctx=Load()),
                                                                    attr='_cached_page',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='page', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                        Return(
                                                            value=Name(id='response', ctx=Load()),
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='KeyError', ctx=Load()),
                                                    name=None,
                                                    body=[Pass()],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='_', ctx=Store()),
                                                Name(id='ext', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='os', ctx=Load()),
                                                attr='path',
                                                ctx=Load(),
                                            ),
                                            attr='splitext',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='req_page', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='render',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='view_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Dict(
                                                keys=[
                                                    Constant(value='deletable', kind=None),
                                                    Constant(value='main_object', kind=None),
                                                ],
                                                values=[
                                                    Constant(value=True, kind=None),
                                                    Name(id='page', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='mimetype',
                                                value=Call(
                                                    func=Name(id='_guess_mimetype', ctx=Load()),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='need_to_cache', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=200, kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='r', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='render',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='page', ctx=Load()),
                                                    attr='_set_cache_response',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='cache_key', ctx=Load()),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='content', kind=None),
                                                            Constant(value='contenttype', kind=None),
                                                            Constant(value='time', kind=None),
                                                            Constant(value='template', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='r', ctx=Load()),
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='response', ctx=Load()),
                                                                    attr='headers',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='Content-Type', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='time',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Name(id='getattr', ctx=Load()),
                                                                        args=[
                                                                            Name(id='response', ctx=Load()),
                                                                            Constant(value='qcontext', kind=None),
                                                                            Dict(keys=[], values=[]),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='response_template', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='response', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_serve_redirect',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='req_page', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='httprequest',
                                    ctx=Load(),
                                ),
                                attr='path',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='redirect_type', kind=None),
                                            Constant(value='in', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='301', kind=None),
                                                    Constant(value='302', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='url_from', kind=None),
                                            Constant(value='=', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='req_page', ctx=Load()),
                                                    attr='rstrip',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='/', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='url_from', kind=None),
                                            Constant(value='=', kind=None),
                                            BinOp(
                                                left=Name(id='req_page', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value='/', kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        AugAssign(
                            target=Name(id='domain', ctx=Store()),
                            op=Add(),
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='website',
                                        ctx=Load(),
                                    ),
                                    attr='website_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.rewrite', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_serve_fallback',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='parent', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_serve_fallback',
                                    ctx=Load(),
                                ),
                                args=[Name(id='exception', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='parent', ctx=Load()),
                            body=[
                                Return(
                                    value=Name(id='parent', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='is_frontend',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='website_page', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_serve_page',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='website_page', ctx=Load()),
                            body=[
                                Return(
                                    value=Name(id='website_page', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='redirect', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_serve_redirect',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='redirect', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='redirect',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_build_url_w_params', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='redirect', ctx=Load()),
                                                        attr='url_to',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='params',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='code',
                                                value=Attribute(
                                                    value=Name(id='redirect', ctx=Load()),
                                                    attr='redirect_type',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_exception_code_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='code', ctx=Store()),
                                        Name(id='values', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_exception_code_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='exception', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='exception', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='NotFound',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='is_publisher',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value='page_404', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='httprequest',
                                                ctx=Load(),
                                            ),
                                            attr='path',
                                            ctx=Load(),
                                        ),
                                        slice=Slice(
                                            lower=Constant(value=1, kind=None),
                                            upper=None,
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
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
                                            Name(id='exception', ctx=Load()),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='exceptions',
                                                    ctx=Load(),
                                                ),
                                                attr='Forbidden',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='exception', ctx=Load()),
                                            attr='description',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='website_visibility_password_required', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='code', ctx=Store())],
                                    value=Constant(value='protected_403', kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='path', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='httprequest',
                                            ctx=Load(),
                                        ),
                                        attr='path',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='code', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_values_500_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='exception', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='View', ctx=Store())],
                            value=Subscript(
                                value=Name(id='env', ctx=Load()),
                                slice=Constant(value='ir.ui.view', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Http', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_values_500_error',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                    Name(id='exception', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='qweb_exception', kind=None),
                                ops=[In()],
                                comparators=[Name(id='values', ctx=Load())],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='exception_template', ctx=Store())],
                                            value=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='exception', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='ValueError', ctx=Load()),
                                            name=None,
                                            body=[
                                                Assign(
                                                    targets=[Name(id='exception_template', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='exception', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='view', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='View', ctx=Load()),
                                            attr='_view_obj',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='exception_template', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='exception', ctx=Load()),
                                                attr='html',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='exception', ctx=Load()),
                                                    attr='html',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='arch',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='view', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='view', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='et', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='view', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='inherit_branding',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='_get_combined_arch',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='node', ctx=Store())],
                                            value=IfExp(
                                                test=Attribute(
                                                    value=Name(id='exception', ctx=Load()),
                                                    attr='path',
                                                    ctx=Load(),
                                                ),
                                                body=Call(
                                                    func=Attribute(
                                                        value=Name(id='et', ctx=Load()),
                                                        attr='xpath',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='exception', ctx=Load()),
                                                            attr='path',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                orelse=Name(id='et', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='line', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='node', ctx=Load()),
                                                        ops=[IsNot()],
                                                        comparators=[Constant(value=None, kind=None)],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='etree', ctx=Load()),
                                                            attr='tostring',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='node', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='encoding',
                                                                value=Constant(value='unicode', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='line', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='view', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='View', ctx=Load()),
                                                                    attr='_views_get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='exception_template', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='v', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Name(id='line', ctx=Load()),
                                                                    ops=[In()],
                                                                    comparators=[
                                                                        Attribute(
                                                                            value=Name(id='v', ctx=Load()),
                                                                            attr='arch',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='view', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Subscript(
                                                                value=Name(id='values', ctx=Load()),
                                                                slice=Constant(value='view', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='view', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='editable', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='uid',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='website',
                                                ctx=Load(),
                                            ),
                                            attr='is_publisher',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_error_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='code', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='code', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='page_404', kind=None),
                                            Constant(value='protected_403', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='code', ctx=Load()),
                                                        attr='split',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='_', kind=None)],
                                                    keywords=[],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='env', ctx=Load()),
                                                        slice=Constant(value='ir.ui.view', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_render_template',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='website.%s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='code', ctx=Load()),
                                                    ),
                                                    Name(id='values', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
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
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_get_error_html',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='code', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
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
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='id', ctx=Load()),
                                            Compare(
                                                left=Name(id='model', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='obj', ctx=Load()),
                                    Compare(
                                        left=Constant(value='website_published', kind=None),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='obj', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Name(id='obj', ctx=Load()),
                                                            attr='_name',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='obj', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='website_published', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
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
                FunctionDef(
                    name='_xmlid_to_obj',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='cls', annotation=None, type_comment=None),
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='xmlid', annotation=None, type_comment=None),
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
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
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
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='website_id', ctx=Load()),
                                    Attribute(
                                        value=Name(id='website_id', ctx=Load()),
                                        attr='theme_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='key', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='xmlid', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='website_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='Attachment', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.attachment', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='user',
                                            ctx=Load(),
                                        ),
                                        attr='share',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='domain', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='public', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='Attachment', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Attachment', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='obj', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Attachment', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='obj', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Name(id='obj', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
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
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_xmlid_to_obj',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='xmlid', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_frontend_session_info',
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
                            targets=[Name(id='session_info', ctx=Store())],
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
                                    attr='get_frontend_session_info',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='session_info', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='is_website_user', kind=None),
                                            Constant(value='geoip_country_code', kind=None),
                                        ],
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='website',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='geoip', kind=None),
                                                            Dict(keys=[], values=[]),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='country_code', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                    attr='has_group',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='website.group_website_publisher', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='session_info', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='website_id', kind=None),
                                                    Constant(value='website_company_id', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='website',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='website',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_cached',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='company_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='session_info', ctx=Load()),
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
            name='ModelConverter',
            bases=[
                Attribute(
                    value=Name(id='ir_http', ctx=Load()),
                    attr='ModelConverter',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='to_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
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
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='value', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='slug_matching', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='value', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='_converter_value', kind=None),
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='value', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='to_url',
                                    ctx=Load(),
                                ),
                                args=[Name(id='value', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='generate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='uid', annotation=None, type_comment=None),
                            arg(arg='dom', annotation=None, type_comment=None),
                            arg(arg='args', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Model', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='uid', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='args', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='current_website_id',
                                        value=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
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
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='safe_eval', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='domain',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='args', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                            attr='copy',
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
                        If(
                            test=Name(id='dom', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='dom', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='Model', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Name(id='record', ctx=Load()),
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
