Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='functools', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='math', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[alias(name='urls', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname='odoo_fields'),
                alias(name='http', asname=None),
                alias(name='tools', asname=None),
                alias(name='_', asname=None),
                alias(name='SUPERUSER_ID', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='AccessError', asname=None),
                alias(name='MissingError', asname=None),
                alias(name='UserError', asname=None),
                alias(name='AccessDenied', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[
                alias(name='content_disposition', asname=None),
                alias(name='Controller', asname=None),
                alias(name='request', asname=None),
                alias(name='route', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='consteq', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
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
            name='pager',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url', annotation=None, type_comment=None),
                    arg(arg='total', annotation=None, type_comment=None),
                    arg(arg='page', annotation=None, type_comment=None),
                    arg(arg='step', annotation=None, type_comment=None),
                    arg(arg='scope', annotation=None, type_comment=None),
                    arg(arg='url_args', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=1, kind=None),
                    Constant(value=30, kind=None),
                    Constant(value=5, kind=None),
                    Constant(value=None, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value=' Generate a dict with required value to render `website.pager` template. This method compute\n        url, page range to display, ... in the pager.\n        :param url : base url of the page link\n        :param total : number total of item to be splitted into pages\n        :param page : current page\n        :param step : item per page\n        :param scope : number of page to display on pager\n        :param url_args : additionnal parameters to add as query params to page url\n        :type url_args : dict\n        :returns dict\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='page_count', ctx=Store())],
                    value=Call(
                        func=Name(id='int', ctx=Load()),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='math', ctx=Load()),
                                    attr='ceil',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='float', ctx=Load()),
                                            args=[Name(id='total', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Div(),
                                        right=Name(id='step', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='page', ctx=Store())],
                    value=Call(
                        func=Name(id='max', ctx=Load()),
                        args=[
                            Constant(value=1, kind=None),
                            Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[
                                            IfExp(
                                                test=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='page', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='isdigit',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                body=Name(id='page', ctx=Load()),
                                                orelse=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Name(id='page_count', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                AugAssign(
                    target=Name(id='scope', ctx=Store()),
                    op=Sub(),
                    value=Constant(value=1, kind=None),
                ),
                Assign(
                    targets=[Name(id='pmin', ctx=Store())],
                    value=Call(
                        func=Name(id='max', ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id='page', ctx=Load()),
                                op=Sub(),
                                right=Call(
                                    func=Name(id='int', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Attribute(
                                                value=Name(id='math', ctx=Load()),
                                                attr='floor',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                BinOp(
                                                    left=Name(id='scope', ctx=Load()),
                                                    op=Div(),
                                                    right=Constant(value=2, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            Constant(value=1, kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='pmax', ctx=Store())],
                    value=Call(
                        func=Name(id='min', ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id='pmin', ctx=Load()),
                                op=Add(),
                                right=Name(id='scope', ctx=Load()),
                            ),
                            Name(id='page_count', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=BinOp(
                            left=Name(id='pmax', ctx=Load()),
                            op=Sub(),
                            right=Name(id='pmin', ctx=Load()),
                        ),
                        ops=[Lt()],
                        comparators=[Name(id='scope', ctx=Load())],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='pmin', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=BinOp(
                                        left=Name(id='pmax', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='scope', ctx=Load()),
                                    ),
                                    ops=[Gt()],
                                    comparators=[Constant(value=0, kind=None)],
                                ),
                                body=BinOp(
                                    left=Name(id='pmax', ctx=Load()),
                                    op=Sub(),
                                    right=Name(id='scope', ctx=Load()),
                                ),
                                orelse=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                FunctionDef(
                    name='get_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='page', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='_url', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='page', ctx=Load()),
                                    ops=[Gt()],
                                    comparators=[Constant(value=1, kind=None)],
                                ),
                                body=BinOp(
                                    left=Constant(value='%s/page/%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='url', ctx=Load()),
                                            Name(id='page', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Name(id='url', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='url_args', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s?%s', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Name(id='_url', ctx=Load()),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='urls', ctx=Load()),
                                                        attr='url_encode',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='url_args', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='_url', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Return(
                    value=Dict(
                        keys=[
                            Constant(value='page_count', kind=None),
                            Constant(value='offset', kind=None),
                            Constant(value='page', kind=None),
                            Constant(value='page_first', kind=None),
                            Constant(value='page_start', kind=None),
                            Constant(value='page_previous', kind=None),
                            Constant(value='page_next', kind=None),
                            Constant(value='page_end', kind=None),
                            Constant(value='page_last', kind=None),
                            Constant(value='pages', kind=None),
                        ],
                        values=[
                            Name(id='page_count', ctx=Load()),
                            BinOp(
                                left=BinOp(
                                    left=Name(id='page', ctx=Load()),
                                    op=Sub(),
                                    right=Constant(value=1, kind=None),
                                ),
                                op=Mult(),
                                right=Name(id='step', ctx=Load()),
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[Name(id='page', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='page', ctx=Load()),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[Constant(value=1, kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=1, kind=None),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[Name(id='pmin', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='pmin', ctx=Load()),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='max', ctx=Load()),
                                                args=[
                                                    Name(id='pmin', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='page', ctx=Load()),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='max', ctx=Load()),
                                        args=[
                                            Name(id='pmin', ctx=Load()),
                                            BinOp(
                                                left=Name(id='page', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Name(id='pmax', ctx=Load()),
                                                    BinOp(
                                                        left=Name(id='page', ctx=Load()),
                                                        op=Add(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[
                                            Name(id='pmax', ctx=Load()),
                                            BinOp(
                                                left=Name(id='page', ctx=Load()),
                                                op=Add(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[Name(id='pmax', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='pmax', ctx=Load()),
                                ],
                            ),
                            Dict(
                                keys=[
                                    Constant(value='url', kind=None),
                                    Constant(value='num', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='get_url', ctx=Load()),
                                        args=[Name(id='page_count', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='page_count', ctx=Load()),
                                ],
                            ),
                            ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='url', kind=None),
                                        Constant(value='num', kind=None),
                                    ],
                                    values=[
                                        Call(
                                            func=Name(id='get_url', ctx=Load()),
                                            args=[Name(id='page_num', ctx=Load())],
                                            keywords=[],
                                        ),
                                        Name(id='page_num', ctx=Load()),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='page_num', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Name(id='pmin', ctx=Load()),
                                                BinOp(
                                                    left=Name(id='pmax', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
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
            name='get_records_pager',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='ids', annotation=None, type_comment=None),
                    arg(arg='current', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                If(
                    test=BoolOp(
                        op=And(),
                        values=[
                            Compare(
                                left=Attribute(
                                    value=Name(id='current', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[Name(id='ids', ctx=Load())],
                            ),
                            BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='current', ctx=Load()),
                                            Constant(value='website_url', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='hasattr', ctx=Load()),
                                        args=[
                                            Name(id='current', ctx=Load()),
                                            Constant(value='access_url', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='attr_name', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Name(id='hasattr', ctx=Load()),
                                    args=[
                                        Name(id='current', ctx=Load()),
                                        Constant(value='access_url', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                body=Constant(value='access_url', kind=None),
                                orelse=Constant(value='website_url', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='idx', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ids', ctx=Load()),
                                    attr='index',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='current', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='prev_record', kind=None),
                                    Constant(value='next_record', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='idx', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='current', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='ids', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Name(id='idx', ctx=Load()),
                                                                    op=Sub(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='attr_name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='idx', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='ids', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        op=Sub(),
                                                        right=Constant(value=1, kind=None),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='getattr', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='current', ctx=Load()),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='ids', ctx=Load()),
                                                                slice=BinOp(
                                                                    left=Name(id='idx', ctx=Load()),
                                                                    op=Add(),
                                                                    right=Constant(value=1, kind=None),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Name(id='attr_name', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Dict(keys=[], values=[]),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='_build_url_w_params',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url_string', annotation=None, type_comment=None),
                    arg(arg='query_params', annotation=None, type_comment=None),
                    arg(arg='remove_duplicates', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value=True, kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Rebuild a string url based on url_string and correctly compute query parameters\n    using those present in the url and those given by query_params. Having duplicates in\n    the final url is optional. For example:\n\n     * url_string = '/my?foo=bar&error=pay'\n     * query_params = {'foo': 'bar2', 'alice': 'bob'}\n     * if remove duplicates: result = '/my?foo=bar2&error=pay&alice=bob'\n     * else: result = '/my?foo=bar&foo=bar2&error=pay&alice=bob'\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='urls', ctx=Load()),
                            attr='url_parse',
                            ctx=Load(),
                        ),
                        args=[Name(id='url_string', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='url_params', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='url', ctx=Load()),
                            attr='decode_query',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='remove_duplicates', ctx=Load()),
                    body=[
                        Assign(
                            targets=[Name(id='url_params', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='url_params', ctx=Load()),
                                    attr='to_dict',
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
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='url_params', ctx=Load()),
                            attr='update',
                            ctx=Load(),
                        ),
                        args=[Name(id='query_params', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='url', ctx=Load()),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='query',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='urls', ctx=Load()),
                                                attr='url_encode',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='url_params', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            attr='to_url',
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
        ClassDef(
            name='CustomerPortal',
            bases=[Name(id='Controller', ctx=Load())],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='MANDATORY_BILLING_FIELDS', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='name', kind=None),
                            Constant(value='phone', kind=None),
                            Constant(value='email', kind=None),
                            Constant(value='street', kind=None),
                            Constant(value='city', kind=None),
                            Constant(value='country_id', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='OPTIONAL_BILLING_FIELDS', ctx=Store())],
                    value=List(
                        elts=[
                            Constant(value='zipcode', kind=None),
                            Constant(value='state_id', kind=None),
                            Constant(value='vat', kind=None),
                            Constant(value='company_name', kind=None),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_items_per_page', ctx=Store())],
                    value=Constant(value=80, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_portal_layout_values',
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
                            value=Constant(value='Values for /my/* templates rendering.\n\n        Does not include the record counts.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sales_user', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
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
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='partner', ctx=Load()),
                                                    attr='user_id',
                                                    ctx=Load(),
                                                ),
                                                attr='_is_public',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='sales_user', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='partner', ctx=Load()),
                                        attr='user_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='sales_user', kind=None),
                                    Constant(value='page_name', kind=None),
                                ],
                                values=[
                                    Name(id='sales_user', ctx=Load()),
                                    Constant(value='home', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_home_portal_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='counters', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Values for /my & /my/home routes template rendering.\n\n        Includes the record count for the displayed badges.\n        where 'coutners' is the list of the displayed badges\n        and so the list to compute.\n        ", kind=None),
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='counters',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='counters', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_home_portal_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='counters', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[Constant(value='/my/counters', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='home',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kw', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_portal_layout_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='portal.portal_my_home', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/my', kind=None),
                                        Constant(value='/my/home', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='account',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='redirect', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_portal_layout_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
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
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='error', kind=None),
                                            Constant(value='error_message', kind=None),
                                        ],
                                        values=[
                                            Dict(keys=[], values=[]),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='post', ctx=Load()),
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
                                        comparators=[Constant(value='POST', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='error', ctx=Store()),
                                                Name(id='error_message', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='details_form_validate',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='post', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='error', kind=None),
                                                    Constant(value='error_message', kind=None),
                                                ],
                                                values=[
                                                    Name(id='error', ctx=Load()),
                                                    Name(id='error_message', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='post', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='error', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=DictComp(
                                                key=Name(id='key', ctx=Load()),
                                                value=Subscript(
                                                    value=Name(id='post', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='key', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='MANDATORY_BILLING_FIELDS',
                                                            ctx=Load(),
                                                        ),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    DictComp(
                                                        key=Name(id='key', ctx=Load()),
                                                        value=Subscript(
                                                            value=Name(id='post', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='key', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='OPTIONAL_BILLING_FIELDS',
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='key', ctx=Load()),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='post', ctx=Load())],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        For(
                                            target=Name(id='field', ctx=Store()),
                                            iter=BinOp(
                                                left=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        List(
                                                            elts=[
                                                                Constant(value='country_id', kind=None),
                                                                Constant(value='state_id', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=BitAnd(),
                                                right=Call(
                                                    func=Name(id='set', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='values', ctx=Load()),
                                                                attr='keys',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Name(id='field', ctx=Load()),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='values', ctx=Load()),
                                                                        slice=Name(id='field', ctx=Load()),
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
                                                            type=None,
                                                            name=None,
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='values', ctx=Load()),
                                                                            slice=Name(id='field', ctx=Load()),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value=False, kind=None),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='update',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='zip', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    attr='pop',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='zipcode', kind=None),
                                                                    Constant(value='', kind=None),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                                        args=[Name(id='redirect', ctx=Load())],
                                                        keywords=[],
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
                                                args=[Constant(value='/my/home', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='countries', ctx=Store())],
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
                                                slice=Constant(value='res.country', kind=None),
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
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='states', ctx=Store())],
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
                                                slice=Constant(value='res.country.state', kind=None),
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
                                args=[List(elts=[], ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='partner', kind=None),
                                            Constant(value='countries', kind=None),
                                            Constant(value='states', kind=None),
                                            Constant(value='has_check_vat', kind=None),
                                            Constant(value='redirect', kind=None),
                                            Constant(value='page_name', kind=None),
                                        ],
                                        values=[
                                            Name(id='partner', ctx=Load()),
                                            Name(id='countries', ctx=Load()),
                                            Name(id='states', ctx=Load()),
                                            Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='check_vat', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='redirect', ctx=Load()),
                                            Constant(value='my_details', kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                    Constant(value='portal.portal_my_details', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Attribute(
                                        value=Name(id='response', ctx=Load()),
                                        attr='headers',
                                        ctx=Load(),
                                    ),
                                    slice=Constant(value='X-Frame-Options', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='DENY', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[
                                List(
                                    elts=[Constant(value='/my/account', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='security',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_portal_layout_values',
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
                                    value=Name(id='values', ctx=Load()),
                                    slice=Constant(value='get_error', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='get_error', ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
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
                                comparators=[Constant(value='POST', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_update_password',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='post', ctx=Load()),
                                                                slice=Constant(value='old', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='post', ctx=Load()),
                                                                slice=Constant(value='new1', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='post', ctx=Load()),
                                                                slice=Constant(value='new2', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='strip',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
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
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='portal.portal_my_security', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Dict(
                                            keys=[Constant(value='X-Frame-Options', kind=None)],
                                            values=[Constant(value='DENY', kind=None)],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='route', ctx=Load()),
                            args=[Constant(value='/my/security', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='user', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[
                                            Constant(value='GET', kind=None),
                                            Constant(value='POST', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_update_password',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='old', annotation=None, type_comment=None),
                            arg(arg='new1', annotation=None, type_comment=None),
                            arg(arg='new2', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='k', ctx=Store()),
                                    Name(id='v', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='old', kind=None),
                                            Name(id='old', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='new1', kind=None),
                                            Name(id='new1', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='new2', kind=None),
                                            Name(id='new2', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='v', ctx=Load()),
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='errors', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='password', kind=None)],
                                                        values=[
                                                            Dict(
                                                                keys=[Name(id='k', ctx=Load())],
                                                                values=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='You cannot leave any password empty.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='new1', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[Name(id='new2', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='errors', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[Constant(value='password', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='new2', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The new password and its confirmation must be identical.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
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
                                                slice=Constant(value='res.users', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='change_password',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='old', ctx=Load()),
                                            Name(id='new1', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UserError', ctx=Load()),
                                    name='e',
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='errors', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='password', kind=None)],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='AccessDenied', ctx=Load()),
                                    name='e',
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='args',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='msg', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Call(
                                                                func=Name(id='AccessDenied', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The old password you provided is incorrect, your password was not changed.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='errors', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[Constant(value='password', kind=None)],
                                                        values=[
                                                            Dict(
                                                                keys=[Constant(value='old', kind=None)],
                                                                values=[Name(id='msg', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='new_token', ctx=Store())],
                            value=Call(
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
                                    attr='_compute_session_token',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        attr='sid',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='request', ctx=Load()),
                                        attr='session',
                                        ctx=Load(),
                                    ),
                                    attr='session_token',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='new_token', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='success', kind=None)],
                                values=[
                                    Dict(
                                        keys=[Constant(value='password', kind=None)],
                                        values=[Constant(value=True, kind=None)],
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
                    name='attachment_add',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='file', annotation=None, type_comment=None),
                            arg(arg='res_model', annotation=None, type_comment=None),
                            arg(arg='res_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Process a file uploaded from the portal chatter and create the\n        corresponding `ir.attachment`.\n\n        The attachment will be created "pending" until the associated message\n        is actually created, and it will be garbage collected otherwise.\n\n        :param name: name of the file to save.\n        :type name: string\n\n        :param file: the file to save\n        :type file: werkzeug.FileStorage\n\n        :param res_model: name of the model of the original document.\n            To check access rights only, it will not be saved here.\n        :type res_model: string\n\n        :param res_id: id of the original document.\n            To check access rights only, it will not be saved here.\n        :type res_id: int\n\n        :param access_token: access_token of the original document.\n            To check access rights only, it will not be saved here.\n        :type access_token: string\n\n        :return: attachment data {id, name, mimetype, file_size, access_token}\n        :rtype: dict\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='res_model', ctx=Load()),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='res_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The document does not exist or you do not have the rights to access it.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='IrAttachment', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.attachment', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='access_token', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
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
                                    args=[Constant(value='base.group_user', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='IrAttachment', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='IrAttachment', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='binary_field_real_user',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='IrAttachment', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='access_token', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='IrAttachment', ctx=Load()),
                                            attr='_generate_access_token',
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
                            targets=[Name(id='attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='IrAttachment', ctx=Load()),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='datas', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='res_id', kind=None),
                                            Constant(value='access_token', kind=None),
                                        ],
                                        values=[
                                            Name(id='name', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='file', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value='mail.compose.message', kind=None),
                                            Constant(value=0, kind=None),
                                            Name(id='access_token', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='data',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='json', ctx=Load()),
                                                attr='dumps',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='attachment', ctx=Load()),
                                                            attr='read',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='mimetype', kind=None),
                                                                    Constant(value='file_size', kind=None),
                                                                    Constant(value='access_token', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=List(
                                            elts=[
                                                Tuple(
                                                    elts=[
                                                        Constant(value='Content-Type', kind=None),
                                                        Constant(value='application/json', kind=None),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/portal/attachment/add', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='POST', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='attachment_remove',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='attachment_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Remove the given `attachment_id`, only if it is in a "pending" state.\n\n        The user must have access right on the attachment or provide a valid\n        `access_token`.\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='attachment_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_document_check_access',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='ir.attachment', kind=None),
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[Name(id='attachment_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='access_token',
                                                value=Name(id='access_token', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='AccessError', ctx=Load()),
                                            Name(id='MissingError', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name='e',
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The attachment does not exist or you do not have the rights to access it.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='attachment_sudo', ctx=Load()),
                                            attr='res_model',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='mail.compose.message', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='attachment_sudo', ctx=Load()),
                                            attr='res_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The attachment %s cannot be removed because it is not in a pending state.', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment_sudo', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='attachment_sudo', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='mail.message', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='attachment_ids', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment_sudo', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The attachment %s cannot be removed because it is linked to a message.', kind=None),
                                                    Attribute(
                                                        value=Name(id='attachment_sudo', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='attachment_sudo', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/portal/attachment/remove', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='details_form_validate',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='error', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='error_message', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field_name', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='MANDATORY_BILLING_FIELDS',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='data', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='field_name', ctx=Load())],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='error', ctx=Load()),
                                                    slice=Name(id='field_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='missing', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='email', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='tools', ctx=Load()),
                                                    attr='single_email_re',
                                                    ctx=Load(),
                                                ),
                                                attr='match',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='data', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='email', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='error', ctx=Load()),
                                            slice=Constant(value='email', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='error', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='error_message', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Invalid Email! Please enter a valid email address.', kind=None)],
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
                            targets=[Name(id='partner', ctx=Store())],
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
                                attr='partner_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='data', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='vat', kind=None)],
                                        keywords=[],
                                    ),
                                    Name(id='partner', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='vat',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='data', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='vat', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='can_edit_vat',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Name(id='hasattr', ctx=Load()),
                                                args=[
                                                    Name(id='partner', ctx=Load()),
                                                    Constant(value='check_vat', kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            body=[
                                                If(
                                                    test=Call(
                                                        func=Attribute(
                                                            value=Name(id='data', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='country_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='data', ctx=Load()),
                                                                    slice=Constant(value='vat', kind=None),
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
                                                                        slice=Constant(value='res.partner', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='fix_eu_vat_number',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='int', ctx=Load()),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='data', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='country_id', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='data', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='vat', kind=None)],
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
                                                Assign(
                                                    targets=[Name(id='partner_dummy', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='new',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='vat', kind=None),
                                                                    Constant(value='country_id', kind=None),
                                                                ],
                                                                values=[
                                                                    Subscript(
                                                                        value=Name(id='data', ctx=Load()),
                                                                        slice=Constant(value='vat', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    IfExp(
                                                                        test=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='data', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Constant(value='country_id', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        body=Call(
                                                                            func=Name(id='int', ctx=Load()),
                                                                            args=[
                                                                                Subscript(
                                                                                    value=Name(id='data', ctx=Load()),
                                                                                    slice=Constant(value='country_id', kind=None),
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        orelse=Constant(value=False, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='partner_dummy', ctx=Load()),
                                                                    attr='check_vat',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='ValidationError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Subscript(
                                                                            value=Name(id='error', ctx=Load()),
                                                                            slice=Constant(value='vat', kind=None),
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Constant(value='error', kind=None),
                                                                    type_comment=None,
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='error_message', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Changing VAT number is not allowed once document(s) have been issued for your account. Please contact us directly for this operation.', kind=None)],
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
                        ),
                        If(
                            test=ListComp(
                                elt=Name(id='err', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='err', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='error', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id='err', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='missing', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='error_message', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Some required fields are empty.', kind=None)],
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
                            targets=[Name(id='unknown', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='k', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='k', ctx=Store()),
                                        iter=Name(id='data', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Name(id='k', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='MANDATORY_BILLING_FIELDS',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='OPTIONAL_BILLING_FIELDS',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='unknown', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='error', ctx=Load()),
                                            slice=Constant(value='common', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='Unknown field', kind=None),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='error_message', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value="Unknown field '%s'", kind=None),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value=',', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='unknown', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='error', ctx=Load()),
                                    Name(id='error_message', ctx=Load()),
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
                    name='_document_check_access',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_name', annotation=None, type_comment=None),
                            arg(arg='document_id', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='document', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='model_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[Name(id='document_id', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='document_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='document', ctx=Load()),
                                            attr='with_user',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='exists',
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
                                operand=Name(id='document_sudo', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='MissingError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='This document does not exist.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='document', ctx=Load()),
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
                                            value=Name(id='document', ctx=Load()),
                                            attr='check_access_rule',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='read', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='AccessError', ctx=Load()),
                                    name=None,
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='access_token', ctx=Load()),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='document_sudo', ctx=Load()),
                                                            attr='access_token',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Name(id='consteq', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='document_sudo', ctx=Load()),
                                                                    attr='access_token',
                                                                    ctx=Load(),
                                                                ),
                                                                Name(id='access_token', ctx=Load()),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[Raise(exc=None, cause=None)],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Name(id='document_sudo', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_page_view_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='document', annotation=None, type_comment=None),
                            arg(arg='access_token', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
                            arg(arg='session_history', annotation=None, type_comment=None),
                            arg(arg='no_breadcrumbs', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Name(id='access_token', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='no_breadcrumbs', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='no_breadcrumbs', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='access_token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='access_token', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='token', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='access_token', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='error', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='error', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='error', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='warning', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='warning', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='warning', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='success', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='success', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='success', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='pid', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='pid', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='pid', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='hash', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='hash', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='kwargs', ctx=Load()),
                                        slice=Constant(value='hash', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='history', ctx=Store())],
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
                                    Name(id='session_history', ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='get_records_pager', ctx=Load()),
                                        args=[
                                            Name(id='history', ctx=Load()),
                                            Name(id='document', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_show_report',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='report_type', annotation=None, type_comment=None),
                            arg(arg='report_ref', annotation=None, type_comment=None),
                            arg(arg='download', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        If(
                            test=Compare(
                                left=Name(id='report_type', ctx=Load()),
                                ops=[NotIn()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='html', kind=None),
                                            Constant(value='pdf', kind=None),
                                            Constant(value='text', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Invalid report type: %s', kind=None),
                                                    Name(id='report_type', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='report_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='request', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='ref',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='report_ref', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='with_user',
                                    ctx=Load(),
                                ),
                                args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='report_sudo', ctx=Load()),
                                        Call(
                                            func=Name(id='type', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='ir.actions.report', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='%s is not the reference of a report', kind=None),
                                                    Name(id='report_ref', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='model', ctx=Load()),
                                    Constant(value='company_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='report_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='report_sudo', ctx=Load()),
                                            attr='with_company',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='model', ctx=Load()),
                                                attr='company_id',
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
                        Assign(
                            targets=[Name(id='method_name', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='_render_qweb_%s', kind=None),
                                op=Mod(),
                                right=Name(id='report_type', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='report', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Call(
                                        func=Name(id='getattr', ctx=Load()),
                                        args=[
                                            Name(id='report_sudo', ctx=Load()),
                                            Name(id='method_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    args=[
                                        List(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='data',
                                            value=Dict(
                                                keys=[Constant(value='report_type', kind=None)],
                                                values=[Name(id='report_type', ctx=Load())],
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reporthttpheaders', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='Content-Type', kind=None),
                                            IfExp(
                                                test=Compare(
                                                    left=Name(id='report_type', ctx=Load()),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='pdf', kind=None)],
                                                ),
                                                body=Constant(value='application/pdf', kind=None),
                                                orelse=Constant(value='text/html', kind=None),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='Content-Length', kind=None),
                                            Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='report', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Name(id='report_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='pdf', kind=None)],
                                    ),
                                    Name(id='download', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='filename', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='%s.pdf', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Attribute(
                                                value=Name(id='re', ctx=Load()),
                                                attr='sub',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='\\W+', kind=None),
                                                Constant(value='-', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='model', ctx=Load()),
                                                        attr='_get_report_base_filename',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='reporthttpheaders', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='Content-Disposition', kind=None),
                                                    Call(
                                                        func=Name(id='content_disposition', ctx=Load()),
                                                        args=[Name(id='filename', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
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
                                    value=Name(id='request', ctx=Load()),
                                    attr='make_response',
                                    ctx=Load(),
                                ),
                                args=[Name(id='report', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='headers',
                                        value=Name(id='reporthttpheaders', ctx=Load()),
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
        FunctionDef(
            name='get_error',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='e', annotation=None, type_comment=None),
                    arg(arg='path', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[Constant(value='', kind=None)],
            ),
            body=[
                Expr(
                    value=Constant(value=" Recursively dereferences `path` (a period-separated sequence of dict\n    keys) in `e` (an error dict or value), returns the final resolution IIF it's\n    an str, otherwise returns None\n    ", kind=None),
                ),
                For(
                    target=Name(id='k', ctx=Store()),
                    iter=IfExp(
                        test=Name(id='path', ctx=Load()),
                        body=Call(
                            func=Attribute(
                                value=Name(id='path', ctx=Load()),
                                attr='split',
                                ctx=Load(),
                            ),
                            args=[Constant(value='.', kind=None)],
                            keywords=[],
                        ),
                        orelse=List(elts=[], ctx=Load()),
                    ),
                    body=[
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='isinstance', ctx=Load()),
                                    args=[
                                        Name(id='e', ctx=Load()),
                                        Name(id='dict', ctx=Load()),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=None, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='e', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='e', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='k', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Call(
                            func=Name(id='isinstance', ctx=Load()),
                            args=[
                                Name(id='e', ctx=Load()),
                                Name(id='str', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        body=Name(id='e', ctx=Load()),
                        orelse=Constant(value=None, kind=None),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
