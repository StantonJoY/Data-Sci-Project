Module(
    body=[
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        ImportFrom(
            module='ast',
            names=[alias(name='literal_eval', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.parser',
            names=[alias(name='parse', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.datastructures',
            names=[alias(name='OrderedMultiDict', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='NotFound', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='http', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.http_routing.models.ir_http',
            names=[alias(name='slug', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.website.controllers.main',
            names=[alias(name='QueryURL', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ClassDef(
            name='WebsiteEventController',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='sitemap_event',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='env', annotation=None, type_comment=None),
                            arg(arg='rule', annotation=None, type_comment=None),
                            arg(arg='qs', annotation=None, type_comment=None),
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
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='qs', ctx=Load()),
                                    ),
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
                                        ops=[In()],
                                        comparators=[Constant(value='/events', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Yield(
                                        value=Dict(
                                            keys=[Constant(value='loc', kind=None)],
                                            values=[Constant(value='/events', kind=None)],
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='events',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='searches', annotation=None, type_comment=None),
                        defaults=[Constant(value=1, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='Event', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='event.event', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='SudoEventType', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.type', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
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
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='date', kind=None),
                                    Constant(value='all', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='tags', kind=None),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='type', kind=None),
                                    Constant(value='all', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='setdefault',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='country', kind=None),
                                    Constant(value='all', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='website', ctx=Store())],
                            value=Attribute(
                                value=Name(id='request', ctx=Load()),
                                attr='website',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='step', ctx=Store())],
                            value=Constant(value=12, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='options', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='displayDescription', kind=None),
                                    Constant(value='displayDetail', kind=None),
                                    Constant(value='displayExtraDetail', kind=None),
                                    Constant(value='displayExtraLink', kind=None),
                                    Constant(value='displayImage', kind=None),
                                    Constant(value='allowFuzzy', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='tags', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='country', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=False, kind=None),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='searches', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='noFuzzy', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='searches', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='date', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='searches', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='tags', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='searches', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='type', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='searches', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='country', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=Constant(value='date_begin', kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='searches', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='date', kind=None),
                                        Constant(value='all', kind=None),
                                    ],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='old', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='order', ctx=Store())],
                                    value=Constant(value='date_begin desc', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='order', ctx=Store())],
                            value=BinOp(
                                left=Constant(value='is_published desc, ', kind=None),
                                op=Add(),
                                right=Name(id='order', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='search', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='search', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='event_count', ctx=Store()),
                                        Name(id='details', ctx=Store()),
                                        Name(id='fuzzy_search_term', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='_search_with_fuzzy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='events', kind=None),
                                    Name(id='search', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=BinOp(
                                            left=Name(id='page', ctx=Load()),
                                            op=Mult(),
                                            right=Name(id='step', ctx=Load()),
                                        ),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='options',
                                        value=Name(id='options', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event_details', ctx=Store())],
                            value=Subscript(
                                value=Name(id='details', ctx=Load()),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event_details', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='results', kind=None),
                                    Name(id='Event', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Subscript(
                                value=Name(id='events', ctx=Load()),
                                slice=Slice(
                                    lower=BinOp(
                                        left=BinOp(
                                            left=Name(id='page', ctx=Load()),
                                            op=Sub(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                        op=Mult(),
                                        right=Name(id='step', ctx=Load()),
                                    ),
                                    upper=BinOp(
                                        left=Name(id='page', ctx=Load()),
                                        op=Mult(),
                                        right=Name(id='step', ctx=Load()),
                                    ),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_search', ctx=Store())],
                            value=IfExp(
                                test=Subscript(
                                    value=Name(id='searches', ctx=Load()),
                                    slice=Constant(value='search', kind=None),
                                    ctx=Load(),
                                ),
                                body=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='name', kind=None),
                                                Constant(value='ilike', kind=None),
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='fuzzy_search_term', ctx=Load()),
                                                        Subscript(
                                                            value=Name(id='searches', ctx=Load()),
                                                            slice=Constant(value='search', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='no_date_domain', ctx=Store())],
                            value=Subscript(
                                value=Name(id='event_details', ctx=Load()),
                                slice=Constant(value='no_date_domain', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dates', ctx=Store())],
                            value=Subscript(
                                value=Name(id='event_details', ctx=Load()),
                                slice=Constant(value='dates', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='date', ctx=Store()),
                            iter=Name(id='dates', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='date', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='old', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='date', ctx=Load()),
                                                    slice=Constant(value=3, kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Event', ctx=Load()),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='expression', ctx=Load()),
                                                                    attr='AND',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='no_date_domain', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            op=Add(),
                                                            right=Name(id='domain_search', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Subscript(
                                                            value=Name(id='date', ctx=Load()),
                                                            slice=Constant(value=2, kind=None),
                                                            ctx=Load(),
                                                        ),
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='no_country_domain', ctx=Store())],
                            value=Subscript(
                                value=Name(id='event_details', ctx=Load()),
                                slice=Constant(value='no_country_domain', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='countries', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Event', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='expression', ctx=Load()),
                                                attr='AND',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='no_country_domain', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='domain_search', ctx=Load()),
                                    ),
                                    List(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='groupby',
                                        value=Constant(value='country_id', kind=None),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Constant(value='country_id', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='countries', ctx=Load()),
                                    attr='insert',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=0, kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='country_id_count', kind=None),
                                            Constant(value='country_id', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Call(
                                                            func=Name(id='int', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='country', ctx=Load()),
                                                                    slice=Constant(value='country_id_count', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='country', ctx=Store()),
                                                                iter=Name(id='countries', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='all', kind=None),
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='All Countries', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='search_tags', ctx=Store())],
                            value=Subscript(
                                value=Name(id='event_details', ctx=Load()),
                                slice=Constant(value='search_tags', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_date', ctx=Store())],
                            value=Subscript(
                                value=Name(id='event_details', ctx=Load()),
                                slice=Constant(value='current_date', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_type', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='current_country', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='searches', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value='all', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current_type', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='SudoEventType', ctx=Load()),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='searches', ctx=Load()),
                                                        slice=Constant(value='type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='searches', ctx=Load()),
                                            slice=Constant(value='country', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='all', kind=None)],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='searches', ctx=Load()),
                                            slice=Constant(value='country', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='online', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='current_country', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='searches', ctx=Load()),
                                                        slice=Constant(value='country', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            targets=[Name(id='pager', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='website', ctx=Load()),
                                    attr='pager',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Constant(value='/event', kind=None),
                                    ),
                                    keyword(
                                        arg='url_args',
                                        value=Name(id='searches', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='total',
                                        value=Name(id='event_count', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='page',
                                        value=Name(id='page', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='step',
                                        value=Name(id='step', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='scope',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='keep', ctx=Store())],
                            value=Call(
                                func=Name(id='QueryURL', ctx=Load()),
                                args=[Constant(value='/event', kind=None)],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=DictComp(
                                            key=Name(id='key', ctx=Load()),
                                            value=Name(id='value', ctx=Load()),
                                            generators=[
                                                comprehension(
                                                    target=Tuple(
                                                        elts=[
                                                            Name(id='key', ctx=Store()),
                                                            Name(id='value', ctx=Store()),
                                                        ],
                                                        ctx=Store(),
                                                    ),
                                                    iter=Call(
                                                        func=Attribute(
                                                            value=Name(id='searches', ctx=Load()),
                                                            attr='items',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    ifs=[
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Compare(
                                                                    left=Name(id='key', ctx=Load()),
                                                                    ops=[Eq()],
                                                                    comparators=[Constant(value='search', kind=None)],
                                                                ),
                                                                Compare(
                                                                    left=Name(id='value', ctx=Load()),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value='all', kind=None)],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='searches', ctx=Load()),
                                    slice=Constant(value='search', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='fuzzy_search_term', ctx=Load()),
                                    Name(id='search', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='current_date', kind=None),
                                    Constant(value='current_country', kind=None),
                                    Constant(value='current_type', kind=None),
                                    Constant(value='event_ids', kind=None),
                                    Constant(value='dates', kind=None),
                                    Constant(value='categories', kind=None),
                                    Constant(value='countries', kind=None),
                                    Constant(value='pager', kind=None),
                                    Constant(value='searches', kind=None),
                                    Constant(value='search_tags', kind=None),
                                    Constant(value='keep', kind=None),
                                    Constant(value='search_count', kind=None),
                                    Constant(value='original_search', kind=None),
                                ],
                                values=[
                                    Name(id='current_date', ctx=Load()),
                                    Name(id='current_country', ctx=Load()),
                                    Name(id='current_type', ctx=Load()),
                                    Name(id='events', ctx=Load()),
                                    Name(id='dates', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.tag.category', kind=None),
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
                                                            Constant(value='is_published', kind=None),
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
                                    Name(id='countries', ctx=Load()),
                                    Name(id='pager', ctx=Load()),
                                    Name(id='searches', ctx=Load()),
                                    Name(id='search_tags', ctx=Load()),
                                    Name(id='keep', ctx=Load()),
                                    Name(id='event_count', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='fuzzy_search_term', ctx=Load()),
                                            Name(id='search', ctx=Load()),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='searches', ctx=Load()),
                                    slice=Constant(value='date', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='old', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='canonical_params', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='OrderedMultiDict', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='old', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_event.index', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
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
                            args=[
                                List(
                                    elts=[
                                        Constant(value='/event', kind=None),
                                        Constant(value='/event/page/<int:page>', kind=None),
                                        Constant(value='/events', kind=None),
                                        Constant(value='/events/page/<int:page>', kind=None),
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
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Name(id='sitemap_event', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='page', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='event', kind=None)],
                                values=[Name(id='event', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='.', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='page', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='page', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='website_event.%s', kind=None),
                                        op=Mod(),
                                        right=Name(id='page', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='seo_object', kind=None),
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
                                            attr='get_template',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='page', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='values', ctx=Load()),
                                            slice=Constant(value='main_object', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='event', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='path', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='re', ctx=Load()),
                                                    attr='sub',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='^website_event\\.', kind=None),
                                                    Constant(value='', kind=None),
                                                    Name(id='page', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='from_template', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='website_event.default_page', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='page', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    BoolOp(
                                                        op=And(),
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
                                                            Constant(value='website.page_404', kind=None),
                                                        ],
                                                    ),
                                                    Constant(value='http_routing.404', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='page', ctx=Load()),
                                    Name(id='values', ctx=Load()),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/page/<path:page>', kind=None)],
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
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='menu_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='menu_id',
                                            ctx=Load(),
                                        ),
                                        attr='child_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='target_url', ctx=Store())],
                                    value=Attribute(
                                        value=Subscript(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='menu_id',
                                                    ctx=Load(),
                                                ),
                                                attr='child_id',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='url',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='target_url', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='/event/%s/register', kind=None),
                                        op=Mod(),
                                        right=Call(
                                            func=Name(id='str', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='event', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='post', ctx=Load()),
                                        attr='get',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='enable_editor', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='1', kind=None)],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='target_url', ctx=Store()),
                                    op=Add(),
                                    value=Constant(value='?enable_editor=1', kind=None),
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
                                args=[Name(id='target_url', ctx=Load())],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>', kind=None)],
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
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='event_register',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
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
                                    attr='_prepare_event_register_values',
                                    ctx=Load(),
                                ),
                                args=[Name(id='event', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='post', ctx=Load()),
                                    ),
                                ],
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
                                    Constant(value='website_event.event_description_full', kind=None),
                                    Name(id='values', ctx=Load()),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/register', kind=None)],
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
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_prepare_event_register_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Return the require values to render the template.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='urls', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='_get_event_resource_urls',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='event', kind=None),
                                    Constant(value='main_object', kind=None),
                                    Constant(value='range', kind=None),
                                    Constant(value='google_url', kind=None),
                                    Constant(value='iCal_url', kind=None),
                                ],
                                values=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='event', ctx=Load()),
                                    Name(id='range', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='google_url', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='iCal_url', kind=None)],
                                        keywords=[],
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
                    name='_process_tickets_form',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='form_details', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Process posted data about ticket order. Generic ticket are supported\n        for event without tickets (generic registration).\n\n        :return: list of order per ticket: [{\n            'id': if of ticket if any (0 if no ticket),\n            'ticket': browse record of ticket if any (None if no ticket),\n            'name': ticket name (or generic 'Registration' name if no ticket),\n            'quantity': number of registrations for that ticket,\n        }, {...}]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ticket_order', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='form_details', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='registration_items', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='key', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='nb_register-', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='registration_items', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=2, kind=None)],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ticket_order', ctx=Load()),
                                            slice=Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='registration_items', ctx=Load()),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='int', ctx=Load()),
                                        args=[Name(id='value', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ticket_dict', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='ticket', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Name(id='ticket', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='ticket', ctx=Store()),
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
                                                                    slice=Constant(value='event.event.ticket', kind=None),
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
                                                                        Constant(value='in', kind=None),
                                                                        ListComp(
                                                                            elt=Name(id='tid', ctx=Load()),
                                                                            generators=[
                                                                                comprehension(
                                                                                    target=Name(id='tid', ctx=Store()),
                                                                                    iter=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ticket_order', ctx=Load()),
                                                                                            attr='keys',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    ifs=[Name(id='tid', ctx=Load())],
                                                                                    is_async=0,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='event_id', kind=None),
                                                                        Constant(value='=', kind=None),
                                                                        Attribute(
                                                                            value=Name(id='event', ctx=Load()),
                                                                            attr='id',
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
                        Return(
                            value=ListComp(
                                elt=Dict(
                                    keys=[
                                        Constant(value='id', kind=None),
                                        Constant(value='ticket', kind=None),
                                        Constant(value='name', kind=None),
                                        Constant(value='quantity', kind=None),
                                    ],
                                    values=[
                                        IfExp(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='ticket_dict', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tid', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=Name(id='tid', ctx=Load()),
                                            orelse=Constant(value=0, kind=None),
                                        ),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='ticket_dict', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Name(id='tid', ctx=Load())],
                                            keywords=[],
                                        ),
                                        IfExp(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='ticket_dict', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='tid', ctx=Load())],
                                                keywords=[],
                                            ),
                                            body=Subscript(
                                                value=Subscript(
                                                    value=Name(id='ticket_dict', ctx=Load()),
                                                    slice=Name(id='tid', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='name', kind=None),
                                                ctx=Load(),
                                            ),
                                            orelse=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Registration', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                        Name(id='count', ctx=Load()),
                                    ],
                                ),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='tid', ctx=Store()),
                                                Name(id='count', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='ticket_order', ctx=Load()),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='count', ctx=Load())],
                                        is_async=0,
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
                    name='registration_new',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tickets', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_tickets_form',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='post', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='availability_check', ctx=Store())],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='event', ctx=Load()),
                                attr='seats_limited',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ordered_seats', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='ticket', ctx=Store()),
                                    iter=Name(id='tickets', ctx=Load()),
                                    body=[
                                        AugAssign(
                                            target=Name(id='ordered_seats', ctx=Store()),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='ticket', ctx=Load()),
                                                slice=Constant(value='quantity', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='event', ctx=Load()),
                                            attr='seats_available',
                                            ctx=Load(),
                                        ),
                                        ops=[Lt()],
                                        comparators=[Name(id='ordered_seats', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='availability_check', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='tickets', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='default_first_attendee', ctx=Store())],
                            value=Dict(keys=[], values=[]),
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
                                        attr='_is_public',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='default_first_attendee', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='email', kind=None),
                                            Constant(value='phone', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='request', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='user',
                                                    ctx=Load(),
                                                ),
                                                attr='email',
                                                ctx=Load(),
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='mobile',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='user',
                                                            ctx=Load(),
                                                        ),
                                                        attr='phone',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='visitor', ctx=Store())],
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
                                            attr='_get_visitor_from_request',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='visitor', ctx=Load()),
                                        attr='email',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='default_first_attendee', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='email', kind=None),
                                                    Constant(value='phone', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='email',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='mobile',
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
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_event.registration_attendee_details', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='tickets', kind=None),
                                            Constant(value='event', kind=None),
                                            Constant(value='availability_check', kind=None),
                                            Constant(value='default_first_attendee', kind=None),
                                        ],
                                        values=[
                                            Name(id='tickets', ctx=Load()),
                                            Name(id='event', ctx=Load()),
                                            Name(id='availability_check', ctx=Load()),
                                            Name(id='default_first_attendee', ctx=Load()),
                                        ],
                                    ),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/registration/new', kind=None)],
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
                    name='_process_attendees_form',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='form_details', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Process data posted from the attendee details form.\n\n        :param form_details: posted data from frontend registration form, like\n            {'1-name': 'r', '1-email': 'r@r.com', '1-phone': '', '1-event_ticket_id': '1'}\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='allowed_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.registration', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_get_website_registration_allowed_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registration_fields', ctx=Store())],
                            value=DictComp(
                                key=Name(id='key', ctx=Load()),
                                value=Name(id='v', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Tuple(
                                            elts=[
                                                Name(id='key', ctx=Store()),
                                                Name(id='v', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                        iter=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='event.registration', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_fields',
                                                    ctx=Load(),
                                                ),
                                                attr='items',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        ifs=[
                                            Compare(
                                                left=Name(id='key', ctx=Load()),
                                                ops=[In()],
                                                comparators=[Name(id='allowed_fields', ctx=Load())],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registrations', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='global_values', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='form_details', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='counter', ctx=Store()),
                                                Name(id='attr_name', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='key', ctx=Load()),
                                            attr='split',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='-', kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_name', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='attr_name', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='-', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='field_name', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='registration_fields', ctx=Load())],
                                    ),
                                    body=[Continue()],
                                    orelse=[
                                        If(
                                            test=Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='registration_fields', ctx=Load()),
                                                        slice=Name(id='field_name', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Many2one',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Integer',
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
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Call(
                                                                func=Name(id='int', ctx=Load()),
                                                                args=[Name(id='value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='value', ctx=Store())],
                                                    value=Name(id='value', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='counter', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='0', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='global_values', ctx=Load()),
                                                    slice=Name(id='attr_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='registrations', ctx=Load()),
                                                            attr='setdefault',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='counter', ctx=Load()),
                                                            Call(
                                                                func=Name(id='dict', ctx=Load()),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Name(id='attr_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='value', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='global_values', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                For(
                                    target=Name(id='registration', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='values',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='registration', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='value', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Name(id='list', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='registrations', ctx=Load()),
                                            attr='values',
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
                    name='_create_attendees_from_registration_post',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='registration_data', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Also try to set a visitor (from request) and\n        a partner (if visitor linked to a user for example). Purpose is to gather\n        as much informations as possible, notably to ease future communications.\n        Also try to update visitor informations based on registration info. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='visitor_sudo', ctx=Store())],
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
                                    attr='_get_visitor_from_request',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='force_create',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='visitor_sudo', ctx=Load()),
                                    attr='_update_visitor_last_visit',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='visitor_values', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='registrations_to_create', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='registration_values', ctx=Store()),
                            iter=Name(id='registration_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='registration_values', ctx=Load()),
                                            slice=Constant(value='event_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='event', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='registration_values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='partner_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            Attribute(
                                                value=Name(id='visitor_sudo', ctx=Load()),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='registration_values', ctx=Load()),
                                                    slice=Constant(value='partner_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='visitor_sudo', ctx=Load()),
                                                    attr='partner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='registration_values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='partner_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='registration_values', ctx=Load()),
                                                            slice=Constant(value='partner_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
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
                                                                attr='_is_public',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        body=Constant(value=False, kind=None),
                                                        orelse=Attribute(
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
                                                            attr='id',
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
                                If(
                                    test=Name(id='visitor_sudo', ctx=Load()),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='registration_values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='name', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='visitor_sudo', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='visitor_values', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='visitor_values', ctx=Load()),
                                                            slice=Constant(value='name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='registration_values', ctx=Load()),
                                                        slice=Constant(value='name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='registration_values', ctx=Load()),
                                                    slice=Constant(value='visitor_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='visitor_sudo', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='registrations_to_create', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='registration_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='visitor_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='visitor_sudo', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='visitor_values', ctx=Load())],
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
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='event.registration', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='registrations_to_create', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='registration_confirm',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='post', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='registrations', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_attendees_form',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='post', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='attendees_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_create_attendees_from_registration_post',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='event', ctx=Load()),
                                    Name(id='registrations', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='redirect',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Constant(value='/event/%s/registration/success?', kind=None),
                                            op=Mod(),
                                            right=Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='werkzeug', ctx=Load()),
                                                    attr='urls',
                                                    ctx=Load(),
                                                ),
                                                attr='url_encode',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Dict(
                                                    keys=[Constant(value='registration_ids', kind=None)],
                                                    values=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Constant(value=',', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                ListComp(
                                                                    elt=Call(
                                                                        func=Name(id='str', ctx=Load()),
                                                                        args=[Name(id='id', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='id', ctx=Store()),
                                                                            iter=Attribute(
                                                                                value=Name(id='attendees_sudo', ctx=Load()),
                                                                                attr='ids',
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
                                                    ],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/registration/confirm', kind=None)],
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
                    name='event_registration_success',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='registration_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='visitor', ctx=Store())],
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
                                    attr='_get_visitor_from_request',
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
                                operand=Name(id='visitor', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='NotFound', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='attendees_sudo', ctx=Store())],
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
                                                slice=Constant(value='event.registration', kind=None),
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
                                                    Constant(value='in', kind=None),
                                                    ListComp(
                                                        elt=Call(
                                                            func=Name(id='str', ctx=Load()),
                                                            args=[Name(id='registration_id', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='registration_id', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='registration_ids', ctx=Load()),
                                                                        attr='split',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[Constant(value=',', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='event_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='visitor_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='visitor', ctx=Load()),
                                                        attr='id',
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
                                    Constant(value='website_event.registration_complete', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_registration_confirm_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='event', ctx=Load()),
                                            Name(id='attendees_sudo', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                            args=[
                                List(
                                    elts=[Constant(value='/event/<model("event.event"):event>/registration/success', kind=None)],
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
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='GET', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                                keyword(
                                    arg='sitemap',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_registration_confirm_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                            arg(arg='attendees_sudo', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='urls', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='event', ctx=Load()),
                                    attr='_get_event_resource_urls',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='attendees', kind=None),
                                    Constant(value='event', kind=None),
                                    Constant(value='google_url', kind=None),
                                    Constant(value='iCal_url', kind=None),
                                ],
                                values=[
                                    Name(id='attendees_sudo', ctx=Load()),
                                    Name(id='event', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='google_url', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='iCal_url', kind=None)],
                                        keywords=[],
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
                    name='add_event',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='event_start', annotation=None, type_comment=None),
                            arg(arg='event_end', annotation=None, type_comment=None),
                            arg(arg='address_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_prepare_event_values',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='event_start', ctx=Load()),
                                    Name(id='event_end', ctx=Load()),
                                    Name(id='address_values', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='event', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.event', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='/event/%s/register?enable_editor=1', kind=None),
                                op=Mod(),
                                right=Call(
                                    func=Name(id='slug', ctx=Load()),
                                    args=[Name(id='event', ctx=Load())],
                                    keywords=[],
                                ),
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
                            args=[Constant(value='/event/add_event', kind=None)],
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
                    name='_prepare_event_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='event_start', annotation=None, type_comment=None),
                            arg(arg='event_end', annotation=None, type_comment=None),
                            arg(arg='address_values', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Return the values to create a new event.\n        event_start,event_date are datetimes in the user tz.\n        address_values is used to either choose an existing location or create one as we allow it in the frontend.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='date_begin', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='parse', ctx=Load()),
                                                args=[Name(id='event_start', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='utc',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='date_end', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='parse', ctx=Load()),
                                                args=[Name(id='event_end', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='astimezone',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='pytz', ctx=Load()),
                                                attr='utc',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='replace',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='tzinfo',
                                        value=Constant(value=None, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='address_id', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='address_values', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='address_pid', ctx=Store()),
                                                Name(id='address_vals', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Tuple(
                                        elts=[
                                            Call(
                                                func=Name(id='int', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='address_values', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Subscript(
                                                value=Name(id='address_values', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='address_id', ctx=Store())],
                                    value=Name(id='address_pid', ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='address_pid', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='address_id', ctx=Store())],
                                            value=Attribute(
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
                                                        attr='create',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='address_vals', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                attr='id',
                                                ctx=Load(),
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
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='date_begin', kind=None),
                                    Constant(value='date_end', kind=None),
                                    Constant(value='address_id', kind=None),
                                    Constant(value='seats_available', kind=None),
                                    Constant(value='website_id', kind=None),
                                    Constant(value='event_ticket_ids', kind=None),
                                ],
                                values=[
                                    Name(id='name', ctx=Load()),
                                    Name(id='date_begin', ctx=Load()),
                                    Name(id='date_end', ctx=Load()),
                                    Name(id='address_id', ctx=Load()),
                                    Constant(value=1000, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='website',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='event.event.ticket', kind=None),
                                        ctx=Load(),
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
                    name='get_country_events',
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
                            targets=[Name(id='Event', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='event.event', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='country_code', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='session',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='geoip', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='country_code', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='events', kind=None),
                                    Constant(value='country', kind=None),
                                ],
                                values=[
                                    List(elts=[], ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='events', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
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
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='country_code', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='country', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='code', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Name(id='country_code', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='events', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Event', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='domain', ctx=Load()),
                                                op=Add(),
                                                right=List(
                                                    elts=[
                                                        Constant(value='|', kind=None),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='address_id', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Constant(value=None, kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='country_id.code', kind=None),
                                                                Constant(value='=', kind=None),
                                                                Name(id='country_code', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='date_begin', kind=None),
                                                                Constant(value='>=', kind=None),
                                                                BinOp(
                                                                    left=Constant(value='%s 00:00:00', kind=None),
                                                                    op=Mod(),
                                                                    right=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='fields', ctx=Load()),
                                                                                attr='Date',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='today',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='date_begin', kind=None),
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
                                operand=Name(id='events', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='events', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Event', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='domain', ctx=Load()),
                                                op=Add(),
                                                right=List(
                                                    elts=[
                                                        Tuple(
                                                            elts=[
                                                                Constant(value='date_begin', kind=None),
                                                                Constant(value='>=', kind=None),
                                                                BinOp(
                                                                    left=Constant(value='%s 00:00:00', kind=None),
                                                                    op=Mod(),
                                                                    right=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='fields', ctx=Load()),
                                                                                attr='Date',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='today',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='date_begin', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='event', ctx=Store()),
                            iter=Name(id='events', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='country_code', ctx=Load()),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='country_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='country_code', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='country', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='country', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Constant(value='events', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='event', kind=None),
                                                    Constant(value='url', kind=None),
                                                ],
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='get_formated_date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='event', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='event', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='event', ctx=Load()),
                                                        attr='website_url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.ui.view', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='website_event.country_events_list', kind=None),
                                    Name(id='result', ctx=Load()),
                                ],
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
                            args=[Constant(value='/event/get_country_event_list', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='json', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
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
                    name='get_formated_date',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='event', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='start_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='date_begin',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='end_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='fields', ctx=Load()),
                                                attr='Datetime',
                                                ctx=Load(),
                                            ),
                                            attr='from_string',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='event', ctx=Load()),
                                                attr='date_end',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='date',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='month', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='babel', ctx=Load()),
                                            attr='dates',
                                            ctx=Load(),
                                        ),
                                        attr='get_month_names',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='abbreviated', kind=None)],
                                    keywords=[
                                        keyword(
                                            arg='locale',
                                            value=Attribute(
                                                value=Call(
                                                    func=Name(id='get_lang', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='event', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='start_date', ctx=Load()),
                                    attr='month',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='%s %s%s', kind=None),
                                op=Mod(),
                                right=Tuple(
                                    elts=[
                                        Name(id='month', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='start_date', ctx=Load()),
                                                attr='strftime',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='%e', kind=None)],
                                            keywords=[],
                                        ),
                                        BoolOp(
                                            op=Or(),
                                            values=[
                                                BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Name(id='end_date', ctx=Load()),
                                                            ops=[NotEq()],
                                                            comparators=[Name(id='start_date', ctx=Load())],
                                                        ),
                                                        BinOp(
                                                            left=Constant(value='-', kind=None),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='end_date', ctx=Load()),
                                                                    attr='strftime',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='%e', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                Constant(value='', kind=None),
                                            ],
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_extract_searched_event_tags',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='searches', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tags', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='request', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='event.tag', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='searches', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='tags', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='tag_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='literal_eval', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='searches', ctx=Load()),
                                                        slice=Constant(value='tags', kind=None),
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
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='tags', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='request', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='event.tag', kind=None),
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
                                                                    Constant(value='id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='tag_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='tags', ctx=Load()),
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
