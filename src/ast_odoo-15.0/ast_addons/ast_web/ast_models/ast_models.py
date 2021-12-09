Module(
    body=[
        Import(
            names=[alias(name='babel.dates', asname=None)],
        ),
        Import(
            names=[alias(name='pytz', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='_lt', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv.expression',
            names=[
                alias(name='AND', asname=None),
                alias(name='TRUE_DOMAIN', asname=None),
                alias(name='normalize_domain', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='date_utils', asname=None),
                alias(name='lazy', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='collections',
            names=[alias(name='defaultdict', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Store())],
            value=Call(
                func=Name(id='_lt', ctx=Load()),
                args=[Constant(value='Too many items to display.', kind=None)],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='is_true_domain',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='domain', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Return(
                    value=Compare(
                        left=Call(
                            func=Name(id='normalize_domain', ctx=Load()),
                            args=[Name(id='domain', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Eq()],
                        comparators=[Name(id='TRUE_DOMAIN', ctx=Load())],
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='lazymapping',
            bases=[Name(id='defaultdict', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__missing__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='key', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='default_factory',
                                    ctx=Load(),
                                ),
                                args=[Name(id='key', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='self', ctx=Load()),
                                    slice=Name(id='key', ctx=Load()),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='value', ctx=Load()),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='value', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        Assign(
            targets=[Name(id='DISPLAY_DATE_FORMATS', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value='day', kind=None),
                    Constant(value='week', kind=None),
                    Constant(value='month', kind=None),
                    Constant(value='quarter', kind=None),
                    Constant(value='year', kind=None),
                ],
                values=[
                    Constant(value='dd MMM yyyy', kind=None),
                    Constant(value="'W'w YYYY", kind=None),
                    Constant(value='MMMM yyyy', kind=None),
                    Constant(value='QQQ yyyy', kind=None),
                    Constant(value='yyyy', kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='IrActionsActWindowView',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='ir.actions.act_window.view', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='view_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection_add',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='qweb', kind=None),
                                                Constant(value='QWeb', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Dict(
                                    keys=[Constant(value='qweb', kind=None)],
                                    values=[Constant(value='cascade', kind=None)],
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Base',
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
                    value=Constant(value='base', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='web_search_read',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='order', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Performs a search_read and a search_count.\n\n        :param domain: search domain\n        :param fields: list of fields to read\n        :param limit: maximum number of records to read\n        :param offset: number of records to skip\n        :param order: columns to sort results\n        :return: {\n            'records': array of read records (result of a call to 'search_read')\n            'length': number of records matching the domain (result of a call to 'search_count')\n        }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Name(id='order', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='records', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='length', kind=None),
                                            Constant(value='records', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0, kind=None),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='limit', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='records', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                            Call(
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
                                                args=[Constant(value='force_search_count', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='length', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='length', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='records', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=Name(id='offset', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='length', kind=None),
                                    Constant(value='records', kind=None),
                                ],
                                values=[
                                    Name(id='length', ctx=Load()),
                                    Name(id='records', ctx=Load()),
                                ],
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
                FunctionDef(
                    name='web_read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                            arg(arg='expand', annotation=None, type_comment=None),
                            arg(arg='expand_limit', annotation=None, type_comment=None),
                            arg(arg='expand_orderby', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Returns the result of a read_group (and optionally search for and read records inside each\n        group), and the total number of groups matching the search domain.\n\n        :param domain: search domain\n        :param fields: list of fields to read (see ``fields``` param of ``read_group``)\n        :param groupby: list of fields to group on (see ``groupby``` param of ``read_group``)\n        :param limit: see ``limit`` param of ``read_group``\n        :param offset: see ``offset`` param of ``read_group``\n        :param orderby: see ``orderby`` param of ``read_group``\n        :param lazy: see ``lazy`` param of ``read_group``\n        :param expand: if true, and groupby only contains one field, read records inside each group\n        :param expand_limit: maximum number of records to read in each group\n        :param expand_orderby: order to apply when reading records in each group\n        :return: {\n            'groups': array of read groups\n            'length': total number of groups\n        }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_web_read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                    Name(id='limit', ctx=Load()),
                                    Name(id='offset', ctx=Load()),
                                    Name(id='orderby', ctx=Load()),
                                    Name(id='lazy', ctx=Load()),
                                    Name(id='expand', ctx=Load()),
                                    Name(id='expand_limit', ctx=Load()),
                                    Name(id='expand_orderby', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='groups', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='length', ctx=Store())],
                                    value=Constant(value=0, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='limit', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='groups', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='length', ctx=Store())],
                                            value=Name(id='limit', ctx=Load()),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='chunk_size', ctx=Store())],
                                            value=Constant(value=100000, kind=None),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Constant(value=True, kind=None),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='more', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='read_group',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='domain', ctx=Load()),
                                                                    List(
                                                                        elts=[Constant(value='display_name', kind=None)],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='groupby', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='offset',
                                                                        value=Name(id='length', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='limit',
                                                                        value=Name(id='chunk_size', ctx=Load()),
                                                                    ),
                                                                    keyword(
                                                                        arg='lazy',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='length', ctx=Store()),
                                                    op=Add(),
                                                    value=Name(id='more', ctx=Load()),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='more', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Name(id='chunk_size', ctx=Load())],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='length', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='groups', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='offset', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='groups', kind=None),
                                    Constant(value='length', kind=None),
                                ],
                                values=[
                                    Name(id='groups', ctx=Load()),
                                    Name(id='length', ctx=Load()),
                                ],
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
                FunctionDef(
                    name='_web_read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                            arg(arg='expand', annotation=None, type_comment=None),
                            arg(arg='expand_limit', annotation=None, type_comment=None),
                            arg(arg='expand_orderby', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=0, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Performs a read_group and optionally a web_search_read for each group.\n        See ``web_read_group`` for params description.\n\n        :returns: array of groups\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='fields', ctx=Load()),
                                    Name(id='groupby', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='offset',
                                        value=Name(id='offset', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='orderby',
                                        value=Name(id='orderby', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='lazy',
                                        value=Name(id='lazy', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='expand', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='groupby', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='group', ctx=Store()),
                                    iter=Name(id='groups', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='__data', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='web_search_read',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='domain',
                                                        value=Subscript(
                                                            value=Name(id='group', ctx=Load()),
                                                            slice=Constant(value='__domain', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='fields',
                                                        value=Name(id='fields', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='offset',
                                                        value=Constant(value=0, kind=None),
                                                    ),
                                                    keyword(
                                                        arg='limit',
                                                        value=Name(id='expand_limit', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='order',
                                                        value=Name(id='expand_orderby', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='groups', ctx=Load()),
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
                FunctionDef(
                    name='read_progress_bar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='group_by', annotation=None, type_comment=None),
                            arg(arg='progress_bar', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Gets the data needed for all the kanban column progressbars.\n        These are fetched alongside read_group operation.\n\n        :param domain - the domain used in the kanban view to filter records\n        :param group_by - the name of the field used to group records into\n                        kanban columns\n        :param progress_bar - the <progressbar/> declaration attributes\n                            (field, colors, sum)\n        :return a dictionnary mapping group_by values to dictionnaries mapping\n                progress bar field values to the related number of records\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group_by_fname', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='group_by', ctx=Load()),
                                        attr='partition',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=':', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_type', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='group_by_fname', ctx=Load()),
                                    ctx=Load(),
                                ),
                                attr='type',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='field_type', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='selection', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='selection_labels', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='fields_get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Name(id='group_by', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='selection', kind=None),
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
                        FunctionDef(
                            name='adapt',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='value', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='field_type', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='selection', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='selection_labels', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='value', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='isinstance', ctx=Load()),
                                        args=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='tuple', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='value', ctx=Load()),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='value', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_read_progress_bar',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    Name(id='group_by', ctx=Load()),
                                    Name(id='progress_bar', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='group_by_value', ctx=Store())],
                                    value=Call(
                                        func=Name(id='str', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='adapt', ctx=Load()),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='group', ctx=Load()),
                                                        slice=Name(id='group_by', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='field_value', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='group', ctx=Load()),
                                        slice=Subscript(
                                            value=Name(id='progress_bar', ctx=Load()),
                                            slice=Constant(value='field', kind=None),
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='group_by_value', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='result', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='group_by_value', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='dict', ctx=Load()),
                                                    attr='fromkeys',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='progress_bar', ctx=Load()),
                                                        slice=Constant(value='colors', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
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
                                        left=Name(id='field_value', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            Subscript(
                                                value=Name(id='result', ctx=Load()),
                                                slice=Name(id='group_by_value', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Name(id='group_by_value', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Name(id='field_value', ctx=Load()),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Subscript(
                                                value=Name(id='group', ctx=Load()),
                                                slice=Constant(value='__count', kind=None),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
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
                FunctionDef(
                    name='_read_progress_bar',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='group_by', annotation=None, type_comment=None),
                            arg(arg='progress_bar', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Implementation of read_progress_bar() that returns results in the\n            format of read_group().\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='fname', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='progress_bar', ctx=Load()),
                                        slice=Constant(value='field', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='read_group',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='domain', ctx=Load()),
                                            List(
                                                elts=[Name(id='fname', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Name(id='group_by', ctx=Load()),
                                                    Name(id='fname', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lazy',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='UserError', ctx=Load()),
                                    name=None,
                                    body=[Pass()],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Assign(
                            targets=[Name(id='group_by_name', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='group_by', ctx=Load()),
                                        attr='partition',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value=':', kind=None)],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_by_modifier', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='group_by', ctx=Load()),
                                                attr='partition',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value=':', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='month', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records_values', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='domain', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Subscript(
                                                value=Name(id='progress_bar', ctx=Load()),
                                                slice=Constant(value='field', kind=None),
                                                ctx=Load(),
                                            ),
                                            Name(id='group_by_name', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_type', ctx=Store())],
                            value=Attribute(
                                value=Subscript(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_fields',
                                        ctx=Load(),
                                    ),
                                    slice=Name(id='group_by_name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                attr='type',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record_values', ctx=Store()),
                            iter=Name(id='records_values', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='group_by_value', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record_values', ctx=Load()),
                                            attr='pop',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='group_by_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='group_by_value', ctx=Load()),
                                            Compare(
                                                left=Name(id='field_type', ctx=Load()),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='date', kind=None),
                                                            Constant(value='datetime', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='locale', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Name(id='get_lang', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='group_by_value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='date_utils', ctx=Load()),
                                                    attr='start_of',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='fields', ctx=Load()),
                                                                attr='Datetime',
                                                                ctx=Load(),
                                                            ),
                                                            attr='to_datetime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group_by_value', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    Name(id='group_by_modifier', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='group_by_value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='pytz', ctx=Load()),
                                                            attr='timezone',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='UTC', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='localize',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='group_by_value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='tz_info', ctx=Store())],
                                            value=Constant(value=None, kind=None),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Name(id='field_type', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='datetime', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_context',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='tz', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='pytz', ctx=Load()),
                                                                attr='all_timezones',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='tz_info', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_context',
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='tz', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='group_by_value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='babel', ctx=Load()),
                                                                attr='dates',
                                                                ctx=Load(),
                                                            ),
                                                            attr='format_datetime',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group_by_value', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='format',
                                                                value=Subscript(
                                                                    value=Name(id='DISPLAY_DATE_FORMATS', ctx=Load()),
                                                                    slice=Name(id='group_by_modifier', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='tzinfo',
                                                                value=Name(id='tz_info', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='locale',
                                                                value=Name(id='locale', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='group_by_value', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='babel', ctx=Load()),
                                                                attr='dates',
                                                                ctx=Load(),
                                                            ),
                                                            attr='format_date',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='group_by_value', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='format',
                                                                value=Subscript(
                                                                    value=Name(id='DISPLAY_DATE_FORMATS', ctx=Load()),
                                                                    slice=Name(id='group_by_modifier', ctx=Load()),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='locale',
                                                                value=Name(id='locale', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='field_type', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='many2many', kind=None)],
                                            ),
                                            Call(
                                                func=Name(id='isinstance', ctx=Load()),
                                                args=[
                                                    Name(id='group_by_value', ctx=Load()),
                                                    Name(id='list', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='group_by_value', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='tuple', ctx=Load()),
                                                                args=[Name(id='group_by_value', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Constant(value=False, kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='record_values', ctx=Load()),
                                            slice=Name(id='group_by', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='group_by_value', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='record_values', ctx=Load()),
                                            slice=Constant(value='__count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=1, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='records_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='qweb_render_view',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Name(id='view_id', ctx=Load()),
                            msg=None,
                        ),
                        Return(
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
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='view_id', ctx=Load()),
                                    Dict(
                                        keys=[
                                            None,
                                            None,
                                        ],
                                        values=[
                                            Call(
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
                                                    attr='_prepare_qcontext',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_qweb_prepare_qcontext',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='view_id', ctx=Load()),
                                                    Name(id='domain', ctx=Load()),
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
                FunctionDef(
                    name='_qweb_prepare_qcontext',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Base qcontext for rendering qweb views bound to this model\n        ', kind=None),
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='model', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='records', kind=None),
                                ],
                                values=[
                                    Name(id='self', ctx=Load()),
                                    Name(id='domain', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Name(id='lazy', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='search',
                                                ctx=Load(),
                                            ),
                                            Name(id='domain', ctx=Load()),
                                        ],
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
                    name='fields_view_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='view_id', annotation=None, type_comment=None),
                            arg(arg='view_type', annotation=None, type_comment=None),
                            arg(arg='toolbar', annotation=None, type_comment=None),
                            arg(arg='submenu', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value='form', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='fields_view_get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='view_id', ctx=Load()),
                                    Name(id='view_type', ctx=Load()),
                                    Name(id='toolbar', ctx=Load()),
                                    Name(id='submenu', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='type', kind=None),
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='qweb', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='root', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='fromstring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='r', ctx=Load()),
                                                slice=Constant(value='arch', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='r', ctx=Load()),
                                            slice=Constant(value='arch', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='etree', ctx=Load()),
                                            attr='tostring',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='etree', ctx=Load()),
                                                    attr='Element',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='qweb', kind=None),
                                                    Attribute(
                                                        value=Name(id='root', ctx=Load()),
                                                        attr='attrib',
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
                        Return(
                            value=Name(id='r', ctx=Load()),
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
                FunctionDef(
                    name='_search_panel_field_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Return the values in the image of the provided domain by field_name.\n\n        :param model_domain: domain whose image is returned\n        :param extra_domain: extra domain to use when counting records associated with field values\n        :param field_name: the name of a field (type many2one or selection)\n        :param enable_counters: whether to set the key '__count' in image values\n        :param only_counters: whether to retrieve information on the model_domain image or only\n                                counts based on model_domain and extra_domain. In the later case,\n                                the counts are set whatever is enable_counters.\n        :param limit: integer, maximal number of values to fetch\n        :param set_limit: boolean, whether to use the provided limit (if any)\n        :return: a dict of the form\n                    {\n                        id: { 'id': id, 'display_name': display_name, ('__count': c,) },\n                        ...\n                    }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='enable_counters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='enable_counters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='only_counters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='only_counters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='extra_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='no_extra', ctx=Store())],
                            value=Call(
                                func=Name(id='is_true_domain', ctx=Load()),
                                args=[Name(id='extra_domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='model_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='model_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='count_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='model_domain', ctx=Load()),
                                            Name(id='extra_domain', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='limit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='set_limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='set_limit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='only_counters', ctx=Load()),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_domain_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field_name', ctx=Load()),
                                            Name(id='count_domain', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='model_domain_image', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_search_panel_domain_image',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='field_name', ctx=Load()),
                                    Name(id='model_domain', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='enable_counters', ctx=Load()),
                                            Name(id='no_extra', ctx=Load()),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='set_limit', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='enable_counters', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='no_extra', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='count_domain_image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_domain_image',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field_name', ctx=Load()),
                                            Name(id='count_domain', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='id', ctx=Store()),
                                            Name(id='values', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='model_domain_image', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='element', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='count_domain_image', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='element', ctx=Load()),
                                                body=Subscript(
                                                    value=Name(id='element', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=0, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='model_domain_image', ctx=Load()),
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
                FunctionDef(
                    name='_search_panel_domain_image',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='set_count', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Return the values in the image of the provided domain by field_name.\n\n        :param domain: domain whose image is returned\n        :param field_name: the name of a field (type many2one or selection)\n        :param set_count: whether to set the key '__count' in image values. Default is False.\n        :param limit: integer, maximal number of values to fetch. Default is False.\n        :return: a dict of the form\n                    {\n                        id: { 'id': id, 'display_name': display_name, ('__count': c,) },\n                        ...\n                    }\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field_name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='many2one', kind=None)],
                            ),
                            body=[
                                FunctionDef(
                                    name='group_id_name',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Name(id='value', ctx=Load()),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='desc', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='fields_get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[Name(id='field_name', ctx=Load())],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Name(id='field_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_name_selection', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='desc', ctx=Load()),
                                                slice=Constant(value='selection', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='group_id_name',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Name(id='value', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='field_name_selection', ctx=Load()),
                                                        slice=Name(id='value', ctx=Load()),
                                                        ctx=Load(),
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
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Name(id='domain', ctx=Load()),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='field_name', ctx=Load()),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
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
                        Assign(
                            targets=[Name(id='groups', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='read_group',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='domain', ctx=Load()),
                                    List(
                                        elts=[Name(id='field_name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                    List(
                                        elts=[Name(id='field_name', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain_image', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Name(id='groups', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='id', ctx=Store()),
                                                Name(id='display_name', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='group_id_name', ctx=Load()),
                                        args=[
                                            Subscript(
                                                value=Name(id='group', ctx=Load()),
                                                slice=Name(id='field_name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='display_name', kind=None),
                                        ],
                                        values=[
                                            Name(id='id', ctx=Load()),
                                            Name(id='display_name', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='set_count', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='group', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='field_name', ctx=Load()),
                                                    op=Add(),
                                                    right=Constant(value='_count', kind=None),
                                                ),
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
                                            value=Name(id='domain_image', ctx=Load()),
                                            slice=Name(id='id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='values', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='domain_image', ctx=Load()),
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
                FunctionDef(
                    name='_search_panel_global_counters',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values_range', annotation=None, type_comment=None),
                            arg(arg='parent_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Modify in place values_range to transform the (local) counts\n        into global counts (local count + children local counts)\n        in case a parent field parent_name has been set on the range values.\n        Note that we save the initial (local) counts into an auxiliary dict\n        before they could be changed in the for loop below.\n\n        :param values_range: dict of the form\n            {\n                id: { 'id': id, '__count': c, parent_name: parent_id, ... }\n                ...\n            }\n        :param parent_name: string, indicates which key determines the parent\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='local_counters', ctx=Store())],
                            value=Call(
                                func=Name(id='lazymapping', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='id', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Subscript(
                                            value=Subscript(
                                                value=Name(id='values_range', ctx=Load()),
                                                slice=Name(id='id', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='__count', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='id', ctx=Store()),
                            iter=Name(id='values_range', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values_range', ctx=Load()),
                                        slice=Name(id='id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='count', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='local_counters', ctx=Load()),
                                        slice=Name(id='id', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='count', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='parent_id', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='values', ctx=Load()),
                                                slice=Name(id='parent_name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        While(
                                            test=Name(id='parent_id', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='values', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='values_range', ctx=Load()),
                                                        slice=Name(id='parent_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Subscript(
                                                        value=Name(id='local_counters', ctx=Load()),
                                                        slice=Name(id='parent_id', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Constant(value='__count', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=Name(id='count', ctx=Load()),
                                                ),
                                                Assign(
                                                    targets=[Name(id='parent_id', ctx=Store())],
                                                    value=Subscript(
                                                        value=Name(id='values', ctx=Load()),
                                                        slice=Name(id='parent_name', ctx=Load()),
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
                            ],
                            orelse=[],
                            type_comment=None,
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
                FunctionDef(
                    name='_search_panel_sanitized_parent_hierarchy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='records', annotation=None, type_comment=None),
                            arg(arg='parent_name', annotation=None, type_comment=None),
                            arg(arg='ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Filter the provided list of records to ensure the following properties of\n        the resulting sublist:\n            1) it is closed for the parent relation\n            2) every record in it is an ancestor of a record with id in ids\n                (if ids = records.ids, that condition is automatically satisfied)\n            3) it is maximal among other sublists with properties 1 and 2.\n\n        :param records, the list of records to filter, the records must have the form\n                        { 'id': id, parent_name: False or (id, display_name),... }\n        :param parent_name, string, indicates which key determines the parent\n        :param ids: list of record ids\n        :return: the sublist of records with the above properties\n        }\n        ", kind=None),
                        ),
                        FunctionDef(
                            name='get_parent_id',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='record', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='value', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Name(id='parent_name', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='value', ctx=Load()),
                                            Subscript(
                                                value=Name(id='value', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
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
                        Assign(
                            targets=[Name(id='allowed_records', ctx=Store())],
                            value=DictComp(
                                key=Subscript(
                                    value=Name(id='record', ctx=Load()),
                                    slice=Constant(value='id', kind=None),
                                    ctx=Load(),
                                ),
                                value=Name(id='record', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='record', ctx=Store()),
                                        iter=Name(id='records', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='records_to_keep', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='id', ctx=Store()),
                            iter=Name(id='ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='record_id', ctx=Store())],
                                    value=Name(id='id', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='ancestor_chain', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='chain_is_fully_included', ctx=Store())],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                While(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='chain_is_fully_included', ctx=Load()),
                                            Name(id='record_id', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='known_status', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='records_to_keep', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='record_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Name(id='known_status', ctx=Load()),
                                                ops=[NotEq()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='chain_is_fully_included', ctx=Store())],
                                                    value=Name(id='known_status', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Break(),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='record', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='allowed_records', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='record_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='record', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='ancestor_chain', ctx=Load()),
                                                            slice=Name(id='record_id', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='record', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='record_id', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='get_parent_id', ctx=Load()),
                                                        args=[Name(id='record', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='chain_is_fully_included', ctx=Store())],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='id', ctx=Store()),
                                            Name(id='record', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='ancestor_chain', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='records_to_keep', ctx=Load()),
                                                    slice=Name(id='id', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='chain_is_fully_included', ctx=Load()),
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
                            value=ListComp(
                                elt=Name(id='rec', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='rec', ctx=Store()),
                                        iter=Name(id='records', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='records_to_keep', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='rec', ctx=Load()),
                                                        slice=Constant(value='id', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
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
                FunctionDef(
                    name='_search_panel_selection_range',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="\n        Return the values of a field of type selection possibly enriched\n        with counts of associated records in domain.\n\n        :param enable_counters: whether to set the key '__count' on values returned.\n                                    Default is False.\n        :param expand: whether to return the full range of values for the selection\n                        field or only the field image values. Default is False.\n        :param field_name: the name of a field of type selection\n        :param model_domain: domain used to determine the field image values and counts.\n                                Default is [].\n        :return: a list of dicts of the form\n                    { 'id': id, 'display_name': display_name, ('__count': c,) }\n                with key '__count' set if enable_counters is True\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='enable_counters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='enable_counters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expand', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='expand', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='enable_counters', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='expand', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain_image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_field_image',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field_name', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='only_counters',
                                                value=Name(id='expand', ctx=Load()),
                                            ),
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
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
                                operand=Name(id='expand', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='domain_image', ctx=Load()),
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
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='selection', ctx=Store())],
                            value=Subscript(
                                value=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='fields_get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[Name(id='field_name', ctx=Load())],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    slice=Name(id='field_name', ctx=Load()),
                                    ctx=Load(),
                                ),
                                slice=Constant(value='selection', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='selection_range', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='value', ctx=Store()),
                                    Name(id='label', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='selection', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='display_name', kind=None),
                                        ],
                                        values=[
                                            Name(id='value', ctx=Load()),
                                            Name(id='label', ctx=Load()),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='enable_counters', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='image_element', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='domain_image', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='value', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='image_element', ctx=Load()),
                                                body=Subscript(
                                                    value=Name(id='image_element', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=0, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='selection_range', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='selection_range', ctx=Load()),
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
                FunctionDef(
                    name='search_panel_select_range',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Return possible values of the field field_name (case select="one"),\n        possibly with counters, and the parent field (if any and required)\n        used to hierarchize them.\n\n        :param field_name: the name of a field;\n            of type many2one or selection.\n        :param category_domain: domain generated by categories. Default is [].\n        :param comodel_domain: domain of field values (if relational). Default is [].\n        :param enable_counters: whether to count records by value. Default is False.\n        :param expand: whether to return the full range of field values in comodel_domain\n                        or only the field image values (possibly filtered and/or completed\n                        with parents if hierarchize is set). Default is False.\n        :param filter_domain: domain generated by filters. Default is [].\n        :param hierarchize: determines if the categories must be displayed hierarchically\n                            (if possible). If set to true and _parent_name is set on the\n                            comodel field, the information necessary for the hierarchization will\n                            be returned. Default is True.\n        :param limit: integer, maximal number of values to fetch. Default is None.\n        :param search_domain: base domain of search. Default is [].\n                        with parents if hierarchize is set)\n        :return: {\n            \'parent_field\': parent field on the comodel of field, or False\n            \'values\': array of dictionaries containing some info on the records\n                        available on the comodel of the field \'field_name\'.\n                        The display name, the __count (how many records with that value)\n                        and possibly parent_field are fetched.\n        }\n        or an object with an error message when limit is defined and is reached.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field_name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='supported_types', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='many2one', kind=None),
                                    Constant(value='selection', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[Name(id='supported_types', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='types', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='ir.model.fields', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_fields',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ttype', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='_description_selection',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only types %(supported_types)s are supported for category (found type %(field_type)s)', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='supported_types',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Constant(value=', ', kind=None),
                                                                attr='join',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                GeneratorExp(
                                                                    elt=Subscript(
                                                                        value=Name(id='types', ctx=Load()),
                                                                        slice=Name(id='t', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                    generators=[
                                                                        comprehension(
                                                                            target=Name(id='t', ctx=Store()),
                                                                            iter=Name(id='supported_types', ctx=Load()),
                                                                            ifs=[],
                                                                            is_async=0,
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Subscript(
                                                            value=Name(id='types', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='field', ctx=Load()),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                            targets=[Name(id='model_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='category_domain', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='filter_domain', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='selection', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_panel_selection_range',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field_name', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='model_domain',
                                                        value=Name(id='model_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='extra_domain',
                                                        value=Name(id='extra_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Comodel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='comodel_name',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='hierarchical_naming',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_names', ctx=Store())],
                            value=List(
                                elts=[Constant(value='display_name', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='hierarchize', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='hierarchize', kind=None),
                                    Constant(value=True, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='parent_name', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='hierarchize', ctx=Load()),
                                    Compare(
                                        left=Attribute(
                                            value=Name(id='Comodel', ctx=Load()),
                                            attr='_parent_name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='Comodel', ctx=Load()),
                                                attr='_fields',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='parent_name', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='Comodel', ctx=Load()),
                                        attr='_parent_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_names', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='parent_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                FunctionDef(
                                    name='get_parent_id',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='record', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Name(id='parent_name', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Return(
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='value', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='value', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='hierarchize', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='comodel_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='comodel_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='enable_counters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='enable_counters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expand', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='expand', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='limit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='enable_counters', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='expand', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain_image', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_field_image',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='field_name', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='model_domain',
                                                value=Name(id='model_domain', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='extra_domain',
                                                value=Name(id='extra_domain', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='only_counters',
                                                value=Name(id='expand', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='set_limit',
                                                value=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='limit', ctx=Load()),
                                                        UnaryOp(
                                                            op=Not(),
                                                            operand=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Name(id='expand', ctx=Load()),
                                                                    Name(id='hierarchize', ctx=Load()),
                                                                    Name(id='comodel_domain', ctx=Load()),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            keyword(
                                                arg=None,
                                                value=Name(id='kwargs', ctx=Load()),
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
                                operand=BoolOp(
                                    op=Or(),
                                    values=[
                                        Name(id='expand', ctx=Load()),
                                        Name(id='hierarchize', ctx=Load()),
                                        Name(id='comodel_domain', ctx=Load()),
                                    ],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='domain_image', ctx=Load()),
                                                    attr='values',
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='limit', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='values', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error_msg', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='parent_field', kind=None),
                                            Constant(value='values', kind=None),
                                        ],
                                        values=[
                                            Name(id='parent_name', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='expand', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='image_element_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='domain_image', ctx=Load()),
                                                    attr='keys',
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
                                    test=Name(id='hierarchize', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='condition', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='parent_of', kind=None),
                                                            Name(id='image_element_ids', ctx=Load()),
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
                                            targets=[Name(id='condition', ctx=Store())],
                                            value=List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Name(id='image_element_ids', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='comodel_domain', ctx=Store())],
                                    value=Call(
                                        func=Name(id='AND', ctx=Load()),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='comodel_domain', ctx=Load()),
                                                    Name(id='condition', ctx=Load()),
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
                        Assign(
                            targets=[Name(id='comodel_records', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Comodel', ctx=Load()),
                                    attr='search_read',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='comodel_domain', ctx=Load()),
                                    Name(id='field_names', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Name(id='limit', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='hierarchize', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='ids', ctx=Store())],
                                    value=IfExp(
                                        test=Name(id='expand', ctx=Load()),
                                        body=ListComp(
                                            elt=Subscript(
                                                value=Name(id='rec', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            generators=[
                                                comprehension(
                                                    target=Name(id='rec', ctx=Store()),
                                                    iter=Name(id='comodel_records', ctx=Load()),
                                                    ifs=[],
                                                    is_async=0,
                                                ),
                                            ],
                                        ),
                                        orelse=Name(id='image_element_ids', ctx=Load()),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='comodel_records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_sanitized_parent_hierarchy',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='comodel_records', ctx=Load()),
                                            Name(id='parent_name', ctx=Load()),
                                            Name(id='ids', ctx=Load()),
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
                                    Name(id='limit', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='comodel_records', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='limit', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error_msg', kind=None)],
                                        values=[
                                            Call(
                                                func=Name(id='str', ctx=Load()),
                                                args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='field_range', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='comodel_records', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='record_id', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='record', ctx=Load()),
                                        slice=Constant(value='id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='id', kind=None),
                                            Constant(value='display_name', kind=None),
                                        ],
                                        values=[
                                            Name(id='record_id', ctx=Load()),
                                            Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Constant(value='display_name', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='hierarchize', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Name(id='parent_name', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='get_parent_id', ctx=Load()),
                                                args=[Name(id='record', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='enable_counters', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='image_element', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='domain_image', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='record_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=IfExp(
                                                test=Name(id='image_element', ctx=Load()),
                                                body=Subscript(
                                                    value=Name(id='image_element', ctx=Load()),
                                                    slice=Constant(value='__count', kind=None),
                                                    ctx=Load(),
                                                ),
                                                orelse=Constant(value=0, kind=None),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='field_range', ctx=Load()),
                                            slice=Name(id='record_id', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='values', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='hierarchize', ctx=Load()),
                                    Name(id='enable_counters', ctx=Load()),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_panel_global_counters',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='field_range', ctx=Load()),
                                            Name(id='parent_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='parent_field', kind=None),
                                    Constant(value='values', kind=None),
                                ],
                                values=[
                                    Name(id='parent_name', ctx=Load()),
                                    Call(
                                        func=Name(id='list', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='field_range', ctx=Load()),
                                                    attr='values',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
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
                FunctionDef(
                    name='search_panel_select_multi_range',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='field_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n        Return possible values of the field field_name (case select="multi"),\n        possibly with counters and groups.\n\n        :param field_name: the name of a filter field;\n            possible types are many2one, many2many, selection.\n        :param category_domain: domain generated by categories. Default is [].\n        :param comodel_domain: domain of field values (if relational)\n                                (this parameter is used in _search_panel_range). Default is [].\n        :param enable_counters: whether to count records by value. Default is False.\n        :param expand: whether to return the full range of field values in comodel_domain\n                        or only the field image values. Default is False.\n        :param filter_domain: domain generated by filters. Default is [].\n        :param group_by: extra field to read on comodel, to group comodel records\n        :param group_domain: dict, one domain for each activated group\n                                for the group_by (if any). Those domains are\n                                used to fech accurate counters for values in each group.\n                                Default is [] (many2one case) or None.\n        :param limit: integer, maximal number of values to fetch. Default is None.\n        :param search_domain: base domain of search. Default is [].\n        :return: {\n            \'values\': a list of possible values, each being a dict with keys\n                \'id\' (value),\n                \'name\' (value label),\n                \'__count\' (how many records with that value),\n                \'group_id\' (value of group), set if a group_by has been provided,\n                \'group_name\' (label of group), set if a group_by has been provided\n        }\n        or an object with an error message when limit is defined and reached.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='field', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_fields',
                                    ctx=Load(),
                                ),
                                slice=Name(id='field_name', ctx=Load()),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='supported_types', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='many2one', kind=None),
                                    Constant(value='many2many', kind=None),
                                    Constant(value='selection', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[NotIn()],
                                comparators=[Name(id='supported_types', ctx=Load())],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Only types %(supported_types)s are supported for filter (found type %(field_type)s)', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='supported_types',
                                                        value=Name(id='supported_types', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='field_type',
                                                        value=Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
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
                            targets=[Name(id='model_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='search_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='extra_domain', ctx=Store())],
                            value=Call(
                                func=Name(id='AND', ctx=Load()),
                                args=[
                                    List(
                                        elts=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='category_domain', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='kwargs', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='filter_domain', kind=None),
                                                    List(elts=[], ctx=Load()),
                                                ],
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='selection', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='values', kind=None)],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_panel_selection_range',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field_name', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='model_domain',
                                                        value=Name(id='model_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='extra_domain',
                                                        value=Name(id='extra_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='Comodel', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='field', ctx=Load()),
                                                attr='comodel_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='hierarchical_naming',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='field_names', ctx=Store())],
                            value=List(
                                elts=[Constant(value='display_name', kind=None)],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='group_by', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='group_by', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='limit', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='limit', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='group_by', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='group_by_field', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='Comodel', ctx=Load()),
                                            attr='_fields',
                                            ctx=Load(),
                                        ),
                                        slice=Name(id='group_by', ctx=Load()),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='field_names', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='group_by', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='group_by_field', ctx=Load()),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='many2one', kind=None)],
                                    ),
                                    body=[
                                        FunctionDef(
                                            name='group_id_name',
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='value', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=[
                                                Return(
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Name(id='value', ctx=Load()),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=False, kind=None),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Not Set', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
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
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='group_by_field', ctx=Load()),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='selection', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='desc', ctx=Store())],
                                                    value=Subscript(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='Comodel', ctx=Load()),
                                                                attr='fields_get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                List(
                                                                    elts=[Name(id='group_by', ctx=Load())],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        slice=Name(id='group_by', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='group_by_selection', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='desc', ctx=Load()),
                                                                slice=Constant(value='selection', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='group_by_selection', ctx=Load()),
                                                            slice=Constant(value=False, kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Not Set', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                FunctionDef(
                                                    name='group_id_name',
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=Tuple(
                                                                elts=[
                                                                    Name(id='value', ctx=Load()),
                                                                    Subscript(
                                                                        value=Name(id='group_by_selection', ctx=Load()),
                                                                        slice=Name(id='value', ctx=Load()),
                                                                        ctx=Load(),
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
                                            orelse=[
                                                FunctionDef(
                                                    name='group_id_name',
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='value', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=[
                                                        Return(
                                                            value=IfExp(
                                                                test=Name(id='value', ctx=Load()),
                                                                body=Tuple(
                                                                    elts=[
                                                                        Name(id='value', ctx=Load()),
                                                                        Name(id='value', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                orelse=Tuple(
                                                                    elts=[
                                                                        Constant(value=False, kind=None),
                                                                        Call(
                                                                            func=Name(id='_', ctx=Load()),
                                                                            args=[Constant(value='Not Set', kind=None)],
                                                                            keywords=[],
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
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='comodel_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='comodel_domain', kind=None),
                                    List(elts=[], ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='enable_counters', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='enable_counters', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='expand', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='kwargs', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='expand', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='many2many', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='comodel_records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Comodel', ctx=Load()),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='comodel_domain', ctx=Load()),
                                            Name(id='field_names', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='expand', ctx=Load()),
                                            Name(id='limit', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='comodel_records', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error_msg', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='group_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='group_domain', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='field_range', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='comodel_records', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record_id', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                ],
                                                values=[
                                                    Name(id='record_id', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Constant(value='display_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='group_by', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='group_id', ctx=Store()),
                                                                Name(id='group_name', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='group_id_name', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=Name(id='group_by', ctx=Load()),
                                                                ctx=Load(),
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
                                                            slice=Constant(value='group_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='group_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='group_name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='group_name', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='enable_counters', ctx=Load()),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='expand', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='search_domain', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='AND', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Name(id='model_domain', ctx=Load()),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Name(id='field_name', ctx=Load()),
                                                                                    Constant(value='in', kind=None),
                                                                                    Name(id='record_id', ctx=Load()),
                                                                                ],
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
                                                Assign(
                                                    targets=[Name(id='local_extra_domain', ctx=Store())],
                                                    value=Name(id='extra_domain', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='group_by', ctx=Load()),
                                                            Name(id='group_domain', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='local_extra_domain', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='AND', ctx=Load()),
                                                                args=[
                                                                    List(
                                                                        elts=[
                                                                            Name(id='local_extra_domain', ctx=Load()),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='group_domain', ctx=Load()),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='json', ctx=Load()),
                                                                                            attr='dumps',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='group_id', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    List(elts=[], ctx=Load()),
                                                                                ],
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
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[Name(id='search_count_domain', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='AND', ctx=Load()),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Name(id='search_domain', ctx=Load()),
                                                                    Name(id='local_extra_domain', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='enable_counters', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='count', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='search_count',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='search_count_domain', ctx=Load())],
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
                                                        operand=Name(id='expand', ctx=Load()),
                                                    ),
                                                    body=[
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Name(id='enable_counters', ctx=Load()),
                                                                    Call(
                                                                        func=Name(id='is_true_domain', ctx=Load()),
                                                                        args=[Name(id='local_extra_domain', ctx=Load())],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='inImage', ctx=Store())],
                                                                    value=Name(id='count', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='inImage', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='search',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Name(id='search_domain', ctx=Load())],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='limit',
                                                                                value=Constant(value=1, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='expand', ctx=Load()),
                                                    Name(id='inImage', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                If(
                                                    test=Name(id='enable_counters', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[
                                                                Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='__count', kind=None),
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='count', ctx=Load()),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='field_range', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='values', ctx=Load())],
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
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='expand', ctx=Load()),
                                            ),
                                            Name(id='limit', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='field_range', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error_msg', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='values', kind=None)],
                                        values=[Name(id='field_range', ctx=Load())],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='type',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='many2one', kind=None)],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='enable_counters', ctx=Load()),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='expand', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='extra_domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='AND', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='extra_domain', ctx=Load()),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='kwargs', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='group_domain', kind=None),
                                                                    List(elts=[], ctx=Load()),
                                                                ],
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
                                        Assign(
                                            targets=[Name(id='domain_image', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_search_panel_field_image',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field_name', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='model_domain',
                                                        value=Name(id='model_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='extra_domain',
                                                        value=Name(id='extra_domain', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='only_counters',
                                                        value=Name(id='expand', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='set_limit',
                                                        value=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Name(id='limit', ctx=Load()),
                                                                UnaryOp(
                                                                    op=Not(),
                                                                    operand=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Name(id='expand', ctx=Load()),
                                                                            Name(id='group_by', ctx=Load()),
                                                                            Name(id='comodel_domain', ctx=Load()),
                                                                        ],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg=None,
                                                        value=Name(id='kwargs', ctx=Load()),
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
                                        operand=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='expand', ctx=Load()),
                                                Name(id='group_by', ctx=Load()),
                                                Name(id='comodel_domain', ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='domain_image', ctx=Load()),
                                                            attr='values',
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
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='limit', ctx=Load()),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='len', ctx=Load()),
                                                            args=[Name(id='values', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Name(id='limit', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Return(
                                                    value=Dict(
                                                        keys=[Constant(value='error_msg', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Name(id='str', ctx=Load()),
                                                                args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='values', kind=None)],
                                                values=[Name(id='values', ctx=Load())],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='expand', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='image_element_ids', ctx=Store())],
                                            value=Call(
                                                func=Name(id='list', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='domain_image', ctx=Load()),
                                                            attr='keys',
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
                                            targets=[Name(id='comodel_domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='AND', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Name(id='comodel_domain', ctx=Load()),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Name(id='image_element_ids', ctx=Load()),
                                                                        ],
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
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='comodel_records', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Comodel', ctx=Load()),
                                            attr='search_read',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='comodel_domain', ctx=Load()),
                                            Name(id='field_names', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='limit', ctx=Load()),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='comodel_records', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='limit', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='error_msg', kind=None)],
                                                values=[
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='SEARCH_PANEL_ERROR_MESSAGE', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='field_range', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='record', ctx=Store()),
                                    iter=Name(id='comodel_records', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='record_id', ctx=Store())],
                                            value=Subscript(
                                                value=Name(id='record', ctx=Load()),
                                                slice=Constant(value='id', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='values', ctx=Store())],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='display_name', kind=None),
                                                ],
                                                values=[
                                                    Name(id='record_id', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Constant(value='display_name', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='group_by', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='group_id', ctx=Store()),
                                                                Name(id='group_name', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='group_id_name', ctx=Load()),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=Name(id='group_by', ctx=Load()),
                                                                ctx=Load(),
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
                                                            slice=Constant(value='group_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='group_id', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='group_name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='group_name', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Name(id='enable_counters', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='image_element', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='domain_image', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='record_id', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='__count', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
                                                        test=Name(id='image_element', ctx=Load()),
                                                        body=Subscript(
                                                            value=Name(id='image_element', ctx=Load()),
                                                            slice=Constant(value='__count', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=0, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='field_range', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='values', kind=None)],
                                        values=[Name(id='field_range', ctx=Load())],
                                    ),
                                ),
                            ],
                            orelse=[],
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
            name='ResCompany',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='res.company', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='companies', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='style_fields', ctx=Store())],
                            value=Set(
                                elts=[
                                    Constant(value='external_report_layout_id', kind=None),
                                    Constant(value='font', kind=None),
                                    Constant(value='primary_color', kind=None),
                                    Constant(value='secondary_color', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=UnaryOp(
                                            op=Not(),
                                            operand=Call(
                                                func=Attribute(
                                                    value=Name(id='style_fields', ctx=Load()),
                                                    attr='isdisjoint',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='values', ctx=Store()),
                                                iter=Name(id='vals_list', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_asset_style',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='companies', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='values', annotation=None, type_comment=None),
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
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='style_fields', ctx=Store())],
                            value=Set(
                                elts=[
                                    Constant(value='external_report_layout_id', kind=None),
                                    Constant(value='font', kind=None),
                                    Constant(value='primary_color', kind=None),
                                    Constant(value='secondary_color', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='style_fields', ctx=Load()),
                                        attr='isdisjoint',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='values', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_update_asset_style',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
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
                FunctionDef(
                    name='_get_asset_style_b64',
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
                            targets=[Name(id='template_style', ctx=Store())],
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
                                args=[Constant(value='web.styles_company_report', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='template_style', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=b'', kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='company_ids', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
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
                            targets=[Name(id='company_styles', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template_style', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='company_ids', kind=None)],
                                        values=[Name(id='company_ids', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='base64', ctx=Load()),
                                    attr='b64encode',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='company_styles', ctx=Load()),
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
                    name='_update_asset_style',
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
                            targets=[Name(id='asset_attachment', ctx=Store())],
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
                                args=[Constant(value='web.asset_styles_company_report', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='asset_attachment', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='asset_attachment', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='asset_attachment', ctx=Load()),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='b64_val', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_asset_style_b64',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='b64_val', ctx=Load()),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='asset_attachment', ctx=Load()),
                                        attr='datas',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='asset_attachment', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='datas', kind=None)],
                                                values=[Name(id='b64_val', ctx=Load())],
                                            ),
                                        ],
                                        keywords=[],
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
