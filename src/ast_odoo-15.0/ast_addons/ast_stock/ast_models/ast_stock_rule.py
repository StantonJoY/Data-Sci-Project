Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='collections',
            names=[
                alias(name='defaultdict', asname=None),
                alias(name='namedtuple', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='dateutil.relativedelta',
            names=[alias(name='relativedelta', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='SUPERUSER_ID', asname=None),
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='registry', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='UserError', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='html_escape', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='split_every', asname=None)],
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
        ClassDef(
            name='ProcurementException',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='An exception raised by ProcurementGroup `run` containing all the faulty\n    procurements.\n    ', kind=None),
                ),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='procurement_exceptions', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=':param procurement_exceptions: a list of tuples containing the faulty\n        procurement and their error messages\n        :type procurement_exceptions: list\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='procurement_exceptions',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='procurement_exceptions', ctx=Load()),
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
            name='StockRule',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' A rule describe what a procurement should do; produce, buy, move, ... ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Stock Rule', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='sequence, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_check_company_auto', ctx=Store())],
                    value=Constant(value=True, kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='default_get',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields_list', annotation=None, type_comment=None),
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
                                    attr='default_get',
                                    ctx=Load(),
                                ),
                                args=[Name(id='fields_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='company_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields_list', ctx=Load())],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='res', ctx=Load()),
                                            slice=Constant(value='company_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            attr='company',
                                            ctx=Load(),
                                        ),
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
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='This field will fill the packing origin and the name of its moves', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='active', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Active', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If unchecked, it will allow you to hide the rule without removing it.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_propagation_option', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='none', kind=None),
                                            Constant(value='Leave Empty', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='propagate', kind=None),
                                            Constant(value='Propagate', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='fixed', kind=None),
                                            Constant(value='Fixed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Propagation of Procurement Group', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='propagate', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='group_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='procurement.group', kind=None),
                            Constant(value='Fixed Procurement Group', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='action', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='selection',
                                value=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='pull', kind=None),
                                                Constant(value='Pull From', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='push', kind=None),
                                                Constant(value='Push To', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='pull_push', kind=None),
                                                Constant(value='Pull & Push', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Action', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=20, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.company', kind=None),
                            Constant(value='Company', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('id', '=?', route_company_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='location_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='Destination Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='location_src_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='Source Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='route_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location.route', kind=None),
                            Constant(value='Route', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='route_company_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='route_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Route Company', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='procure_method', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='make_to_stock', kind=None),
                                            Constant(value='Take From Stock', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='make_to_order', kind=None),
                                            Constant(value='Trigger Another Rule', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='mts_else_mto', kind=None),
                                            Constant(value='Take From Stock, if unavailable, Trigger Another Rule', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Supply Method', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='make_to_stock', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Take From Stock: the products will be taken from the available stock of the source location.\nTrigger Another Rule: the system will try to find a stock rule to bring the products in the source location. The available stock will be ignored.\nTake From Stock, if Unavailable, Trigger Another Rule: the products will be taken from the available stock of the source location.If there is no stock available, the system will try to find a  rule to bring the products in the source location.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='route_sequence', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Route Sequence', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='route_id.sequence', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute_sudo',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Operation Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('code', '=?', picking_type_code_domain)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_type_code_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_picking_type_code_domain', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='delay', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lead Time', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The expected date of the created transfer will be computed based on this lead time.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_address_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Partner Address', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Address where goods should be delivered. Optional.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='propagate_cancel', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Cancel Next Move', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When ticked, if the move created by this rule is cancelled, the next move will be cancelled too.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='propagate_carrier', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Propagation of carrier', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When ticked, carrier of shipment will be propgated.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='warehouse_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.warehouse', kind=None),
                            Constant(value='Warehouse', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='propagate_warehouse_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.warehouse', kind=None),
                            Constant(value='Warehouse to Propagate', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The warehouse to propagate on the created move/procurement, which can be different of the warehouse this rule is for (e.g for resupplying rules from another warehouse)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='auto', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='manual', kind=None),
                                            Constant(value='Manual Operation', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='transparent', kind=None),
                                            Constant(value='Automatic No Step Added', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Automatic Move', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='manual', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The 'Manual Operation' value will create a stock move after the current one. With 'Automatic No Step Added', the location is replaced in the original move.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='rule_message', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_action_message', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_picking_type',
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
                            value=Constant(value=" Modify locations to the default picking type's locations source and\n        destination.\n        Enable the delay alert if the picking type is a delivery\n        ", kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='location_src_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='default_location_src_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='location_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_type_id',
                                        ctx=Load(),
                                    ),
                                    attr='default_location_dest_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='picking_type_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_route',
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
                            value=Constant(value=" Ensure that the rule's company is the same than the route's company. ", kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='route_id',
                                    ctx=Load(),
                                ),
                                attr='company_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='company_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='route_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='warehouse_id',
                                        ctx=Load(),
                                    ),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                ops=[NotEq()],
                                comparators=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='route_id',
                                            ctx=Load(),
                                        ),
                                        attr='company_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='route_id', kind=None),
                                Constant(value='company_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_message_values',
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
                            value=Constant(value=' Return the source, destination and picking_type applied on a stock\n        rule. The purpose of this function is to avoid code duplication in\n        _get_message_dict functions since it often requires those data.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='source', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_src_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_src_id',
                                                    ctx=Load(),
                                                ),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Source Location', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='destination', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                                attr='display_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Destination Location', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='operation', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='picking_type_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='picking_type_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Operation Type', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='source', ctx=Load()),
                                    Name(id='destination', ctx=Load()),
                                    Name(id='operation', ctx=Load()),
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
                    name='_get_message_dict',
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
                            value=Constant(value=' Return a dict with the different possible message used for the\n        rule message. It should return one message for each stock.rule action\n        (except push and pull). This function is override in mrp and\n        purchase_stock in order to complete the dictionary.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message_dict', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='source', ctx=Store()),
                                        Name(id='destination', ctx=Store()),
                                        Name(id='operation', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_message_values',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value='push', kind=None),
                                            Constant(value='pull', kind=None),
                                            Constant(value='pull_push', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='suffix', ctx=Store())],
                                    value=Constant(value='', kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='procure_method',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='make_to_order', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_src_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='suffix', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='<br>A need is created in <b>%s</b> and a rule will be triggered to fulfill it.', kind=None),
                                                    Name(id='source', ctx=Load()),
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
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='procure_method',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='mts_else_mto', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_src_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='suffix', ctx=Store())],
                                            value=Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='<br>If the products are not available in <b>%s</b>, a rule will be triggered to bring products in this location.', kind=None),
                                                    Name(id='source', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='message_dict', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='pull', kind=None),
                                            Constant(value='push', kind=None),
                                        ],
                                        values=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='When products are needed in <b>%s</b>, <br/> <b>%s</b> are created from <b>%s</b> to fulfill the need.', kind=None),
                                                        Name(id='destination', ctx=Load()),
                                                        Name(id='operation', ctx=Load()),
                                                        Name(id='source', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Name(id='suffix', ctx=Load()),
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='When products arrive in <b>%s</b>, <br/> <b>%s</b> are created to send them in <b>%s</b>.', kind=None),
                                                    Name(id='source', ctx=Load()),
                                                    Name(id='operation', ctx=Load()),
                                                    Name(id='destination', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='message_dict', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_action_message',
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
                            value=Constant(value=' Generate dynamicaly a message that describe the rule purpose to the\n        end user.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='action_rules', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='rule', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='action',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='rule', ctx=Store()),
                            iter=Name(id='action_rules', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='message_dict', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='_get_message_dict',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='message_dict', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='action',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='message_dict', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='action',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='action',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='pull_push', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message', ctx=Store())],
                                            value=BinOp(
                                                left=BinOp(
                                                    left=Subscript(
                                                        value=Name(id='message_dict', ctx=Load()),
                                                        slice=Constant(value='pull', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    op=Add(),
                                                    right=Constant(value='<br/><br/>', kind=None),
                                                ),
                                                op=Add(),
                                                right=Subscript(
                                                    value=Name(id='message_dict', ctx=Load()),
                                                    slice=Constant(value='push', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='rule_message',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='message', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=BinOp(
                                        left=Name(id='self', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='action_rules', ctx=Load()),
                                    ),
                                    attr='rule_message',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
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
                                Constant(value='action', kind=None),
                                Constant(value='location_id', kind=None),
                                Constant(value='location_src_id', kind=None),
                                Constant(value='picking_type_id', kind=None),
                                Constant(value='procure_method', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_picking_type_code_domain',
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
                                    attr='picking_type_code_domain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='action', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_push',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Apply a push rule on a move.\n        If the rule is 'no step added' it will modify the destination location\n        on the move.\n        If the rule is 'manual operation' it will generate a new move in order\n        to complete the section define by the rule.\n        Care this function is not call by method run. It is called explicitely\n        in stock_move.py inside the method _push_apply\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='new_date', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='date',
                                            ctx=Load(),
                                        ),
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='delay',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='auto',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='transparent', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='old_dest_location', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='location_dest_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='date', kind=None),
                                                    Constant(value='location_dest_id', kind=None),
                                                ],
                                                values=[
                                                    Name(id='new_date', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='location_id',
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
                                If(
                                    test=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='move_line_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='move_line_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='location_dest_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='location_dest_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_get_putaway_strategy',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Name(id='old_dest_location', ctx=Load())],
                                    ),
                                    body=[
                                        Return(
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='move', ctx=Load()),
                                                        attr='_push_apply',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                slice=Slice(
                                                    lower=None,
                                                    upper=Constant(value=1, kind=None),
                                                    step=None,
                                                ),
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='new_move_vals', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_push_prepare_move_copy_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='move', ctx=Load()),
                                            Name(id='new_date', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='new_move', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='copy',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='new_move_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='new_move', ctx=Load()),
                                            attr='_should_bypass_reservation',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_move', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='procure_method', kind=None)],
                                                        values=[Constant(value='make_to_stock', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='new_move', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                                attr='should_bypass_reservation',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='move_dest_ids', kind=None)],
                                                        values=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=4, kind=None),
                                                                            Attribute(
                                                                                value=Name(id='new_move', ctx=Load()),
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
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='new_move', ctx=Load()),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_push_prepare_move_copy_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='move_to_copy', annotation=None, type_comment=None),
                            arg(arg='new_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='company_id', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='company_id',
                                    ctx=Load(),
                                ),
                                attr='id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='company_id', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_id', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='sudo',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                attr='warehouse_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='warehouse_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='new_move_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='origin', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='picking_id', kind=None),
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='propagate_cancel', kind=None),
                                    Constant(value='warehouse_id', kind=None),
                                    Constant(value='procure_method', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='move_to_copy', ctx=Load()),
                                                attr='origin',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move_to_copy', ctx=Load()),
                                                    attr='picking_id',
                                                    ctx=Load(),
                                                ),
                                                attr='name',
                                                ctx=Load(),
                                            ),
                                            Constant(value='/', kind=None),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='move_to_copy', ctx=Load()),
                                            attr='location_dest_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='new_date', ctx=Load()),
                                    Name(id='company_id', ctx=Load()),
                                    Constant(value=False, kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='propagate_cancel',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='warehouse_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='make_to_order', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='new_move_vals', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_run_pull',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='procurements', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='moves_values_by_company', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mtso_products_by_locations', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='procurement', ctx=Store()),
                                    Name(id='rule', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='procurements', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='location_src_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='msg', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='No source location defined on stock rule: %s!', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ProcurementException', ctx=Load()),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='procurement', ctx=Load()),
                                                                    Name(id='msg', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
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
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='procure_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mts_else_mto', kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='mtso_products_by_locations', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='location_src_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='procurement', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
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
                        Assign(
                            targets=[Name(id='forecasted_qties_by_loc', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='location', ctx=Store()),
                                    Name(id='product_ids', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='mtso_products_by_locations', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='products', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='product.product', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='product_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='location',
                                                value=Attribute(
                                                    value=Name(id='location', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='forecasted_qties_by_loc', ctx=Load()),
                                            slice=Name(id='location', ctx=Load()),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=DictComp(
                                        key=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        value=Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='free_qty',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='product', ctx=Store()),
                                                iter=Name(id='products', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='procurements', ctx=Store())],
                            value=Call(
                                func=Name(id='sorted', ctx=Load()),
                                args=[Name(id='procurements', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='key',
                                        value=Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='proc', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Subscript(
                                                                value=Name(id='proc', ctx=Load()),
                                                                slice=Constant(value=0, kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value=0.0, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Subscript(
                                                                        value=Name(id='proc', ctx=Load()),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='product_uom',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='rounding',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='procurement', ctx=Store()),
                                    Name(id='rule', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='procurements', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='procure_method', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='rule', ctx=Load()),
                                        attr='procure_method',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='procure_method',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='mts_else_mto', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_needed', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='procurement', ctx=Load()),
                                                        attr='product_uom',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='procurement', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='procurement', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Name(id='qty_needed', ctx=Load()),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='procurement', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='rounding',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                ops=[LtE()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Subscript(
                                                            value=Name(id='forecasted_qties_by_loc', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='location_src_id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        slice=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='procurement', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=Sub(),
                                                    value=Name(id='qty_needed', ctx=Load()),
                                                ),
                                                Assign(
                                                    targets=[Name(id='procure_method', ctx=Store())],
                                                    value=Constant(value='make_to_order', kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Name(id='qty_needed', ctx=Load()),
                                                                Subscript(
                                                                    value=Subscript(
                                                                        value=Name(id='forecasted_qties_by_loc', ctx=Load()),
                                                                        slice=Attribute(
                                                                            value=Name(id='rule', ctx=Load()),
                                                                            attr='location_src_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='procurement', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='procurement', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='uom_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='rounding',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='procure_method', ctx=Store())],
                                                            value=Constant(value='make_to_order', kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        AugAssign(
                                                            target=Subscript(
                                                                value=Subscript(
                                                                    value=Name(id='forecasted_qties_by_loc', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='rule', ctx=Load()),
                                                                        attr='location_src_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='procurement', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Store(),
                                                            ),
                                                            op=Sub(),
                                                            value=Name(id='qty_needed', ctx=Load()),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='procure_method', ctx=Store())],
                                                            value=Constant(value='make_to_stock', kind=None),
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
                                    targets=[Name(id='move_values', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='rule', ctx=Load()),
                                            attr='_get_stock_move_values',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Name(id='procurement', ctx=Load()),
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
                                            value=Name(id='move_values', ctx=Load()),
                                            slice=Constant(value='procure_method', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='procure_method', ctx=Load()),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Name(id='moves_values_by_company', ctx=Load()),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='procurement', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='move_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='company_id', ctx=Store()),
                                    Name(id='moves_values', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='moves_values_by_company', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='moves', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='stock.move', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Name(id='SUPERUSER_ID', ctx=Load())],
                                                                keywords=[],
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='with_company',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='company_id', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='moves_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='moves', ctx=Load()),
                                            attr='_action_confirm',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                    name='_get_custom_move_fields',
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
                            value=Constant(value=" The purpose of this method is to be override in order to easily add\n        fields from procurement 'values' argument to move data.\n        ", kind=None),
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_stock_move_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='product_qty', annotation=None, type_comment=None),
                            arg(arg='product_uom', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='name', annotation=None, type_comment=None),
                            arg(arg='origin', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
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
                            value=Constant(value=" Returns a dictionary of values that will be used to create a stock move from a procurement.\n        This function assumes that the given procurement has a rule (action == 'pull' or 'pull_push') set on it.\n\n        :param procurement: browse record\n        :rtype: dictionary\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='group_id', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='group_propagation_option',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='propagate', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='group_id', ctx=Store())],
                                    value=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='group_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='group_propagation_option',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='fixed', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='group_id', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='group_id',
                                                    ctx=Load(),
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
                        ),
                        Assign(
                            targets=[Name(id='date_scheduled', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='to_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Call(
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
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='date_planned', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='relativedelta', ctx=Load()),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='days',
                                                    value=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='delay',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                    ),
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
                            targets=[Name(id='date_deadline', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='date_deadline', kind=None)],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='fields', ctx=Load()),
                                                            attr='Datetime',
                                                            ctx=Load(),
                                                        ),
                                                        attr='to_datetime',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='date_deadline', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Call(
                                                    func=Name(id='relativedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='days',
                                                            value=BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='delay',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value=0, kind=None),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='partner_address_id',
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='group_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='group_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='product_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='product_id', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='partner', ctx=Load()),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='lang',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='picking_description', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='_get_description',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_type_id',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='values', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='product_description_variants', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='picking_description', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='product_description_variants', kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='qty_left', ctx=Store())],
                            value=Name(id='product_qty', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='move_dest_ids', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        attr='should_bypass_reservation',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_dest_ids', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='values', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value='move_dest_ids', kind=None),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Constant(value=4, kind=None),
                                                                Attribute(
                                                                    value=Name(id='x', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='x', ctx=Store()),
                                                                iter=Subscript(
                                                                    value=Name(id='values', ctx=Load()),
                                                                    slice=Constant(value='move_dest_ids', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='partner', ctx=Load()),
                                    ),
                                    Name(id='move_dest_ids', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='move_dest', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='move_dest_ids', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='location_id', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='internal_transit_location_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partners', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='move_dest', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='warehouse_id',
                                                    ctx=Load(),
                                                ),
                                                attr='partner_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[Name(id='partners', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=1, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='partner', ctx=Store())],
                                                    value=Name(id='partners', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move_dest', ctx=Load()),
                                                            attr='partner_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Name(id='partner', ctx=Load()),
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
                        ),
                        Assign(
                            targets=[Name(id='move_values', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='partner_id', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='move_dest_ids', kind=None),
                                    Constant(value='rule_id', kind=None),
                                    Constant(value='procure_method', kind=None),
                                    Constant(value='origin', kind=None),
                                    Constant(value='picking_type_id', kind=None),
                                    Constant(value='group_id', kind=None),
                                    Constant(value='route_ids', kind=None),
                                    Constant(value='warehouse_id', kind=None),
                                    Constant(value='date', kind=None),
                                    Constant(value='date_deadline', kind=None),
                                    Constant(value='propagate_cancel', kind=None),
                                    Constant(value='description_picking', kind=None),
                                    Constant(value='priority', kind=None),
                                    Constant(value='orderpoint_id', kind=None),
                                    Constant(value='product_packaging_id', kind=None),
                                ],
                                values=[
                                    Subscript(
                                        value=Name(id='name', ctx=Load()),
                                        slice=Slice(
                                            lower=None,
                                            upper=Constant(value=2000, kind=None),
                                            step=None,
                                        ),
                                        ctx=Load(),
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='location_src_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='company_id', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Attribute(
                                        value=Name(id='product_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='product_uom', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='qty_left', ctx=Load()),
                                    IfExp(
                                        test=Name(id='partner', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='partner', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='location_src_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='location_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='move_dest_ids', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='procure_method',
                                        ctx=Load(),
                                    ),
                                    Name(id='origin', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='picking_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='group_id', ctx=Load()),
                                    ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Constant(value=4, kind=None),
                                                Attribute(
                                                    value=Name(id='route', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='route', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='values', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Constant(value='route_ids', kind=None),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='propagate_warehouse_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='warehouse_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Name(id='date_scheduled', ctx=Load()),
                                    IfExp(
                                        test=Compare(
                                            left=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='group_propagation_option',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Constant(value='fixed', kind=None)],
                                        ),
                                        body=Constant(value=False, kind=None),
                                        orelse=Name(id='date_deadline', ctx=Load()),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='propagate_cancel',
                                        ctx=Load(),
                                    ),
                                    Name(id='picking_description', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='priority', kind=None),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='orderpoint_id', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='orderpoint_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='product_packaging_id', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='product_packaging_id', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_custom_move_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='field', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='values', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='move_values', ctx=Load()),
                                                    slice=Name(id='field', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='field', ctx=Load())],
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
                        Return(
                            value=Name(id='move_values', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_lead_days',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='values', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Returns the cumulative delay and its description encountered by a\n        procurement going through the rules in `self`.\n\n        :param product: the product of the procurement\n        :type product: :class:`~odoo.addons.product.models.product.ProductProduct`\n        :return: the cumulative delay and cumulative delay's description\n        :rtype: tuple[int, list[str, str]]\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='delay', ctx=Store())],
                            value=Call(
                                func=Name(id='sum', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='r', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='r', ctx=Load()),
                                                                attr='action',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='pull', kind=None),
                                                                        Constant(value='pull_push', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='delay', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
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
                                args=[Constant(value='bypass_delay_description', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='delay_description', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='delay_description', ctx=Store())],
                                    value=ListComp(
                                        elt=Tuple(
                                            elts=[
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='Delay on %s', kind=None),
                                                        Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[
                                                        Constant(value='+ %d day(s)', kind=None),
                                                        Attribute(
                                                            value=Name(id='rule', ctx=Load()),
                                                            attr='delay',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='rule', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='rule', ctx=Load()),
                                                                    attr='action',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[
                                                                    List(
                                                                        elts=[
                                                                            Constant(value='pull', kind=None),
                                                                            Constant(value='pull_push', kind=None),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='rule', ctx=Load()),
                                                                attr='delay',
                                                                ctx=Load(),
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
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='delay', ctx=Load()),
                                    Name(id='delay_description', ctx=Load()),
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
        ClassDef(
            name='ProcurementGroup',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='\n    The procurement group class is used to group products together\n    when computing procurements. (tasks, physical products, ...)\n\n    The goal is that when you have one sales order of several products\n    and the products are pulled from the same or several location(s), to keep\n    having the moves grouped into pickings that represent the sales order.\n\n    Used in: sales order (to group delivery order lines like the so), pull/push\n    rules (to pack like the delivery order), on orderpoints (e.g. for wave picking\n    all the similar products together).\n\n    Grouping is made only if the source and the destination is the same.\n    Suppose you have 4 lines on a picking from Output where 2 lines will need\n    to come from Input (crossdock) and 2 lines coming from Stock -> Output As\n    the four will have the same group ids from the SO, the move from input will\n    have a stock.picking with 2 grouped lines and the move from stock will have\n    2 grouped lines also.\n\n    The name is usually the name of the original document (sales order) or a\n    sequence computed if created manually.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='procurement.group', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Procurement Group', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='id desc', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='Procurement', ctx=Store())],
                    value=Call(
                        func=Name(id='namedtuple', ctx=Load()),
                        args=[
                            Constant(value='Procurement', kind=None),
                            List(
                                elts=[
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_qty', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='name', kind=None),
                                    Constant(value='origin', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='values', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='partner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Partner', kind=None),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reference', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='ir.sequence', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='next_by_code',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='procurement.group', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='', kind=None),
                                        ],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='direct', kind=None),
                                            Constant(value='Partial', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='one', kind=None),
                                            Constant(value='All at once', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Delivery Type', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='direct', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='stock_move_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='group_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Related Stock Moves', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='run',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='procurements', annotation=None, type_comment=None),
                            arg(arg='raise_user_error', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=True, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Fulfil `procurements` with the help of stock rules.\n\n        Procurements are needs of products at a certain location. To fulfil\n        these needs, we need to create some sort of documents (`stock.move`\n        by default, but extensions of `_run_` methods allow to create every\n        type of documents).\n\n        :param procurements: the description of the procurement\n        :type list: list of `~odoo.addons.stock.models.stock_rule.ProcurementGroup.Procurement`\n        :param raise_user_error: will raise either an UserError or a ProcurementException\n        :type raise_user_error: boolan, optional\n        :raises UserError: if `raise_user_error` is True and a procurement isn't fulfillable\n        :raises ProcurementException: if `raise_user_error` is False and a procurement isn't fulfillable\n        ", kind=None),
                        ),
                        FunctionDef(
                            name='raise_exception',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='procurement_errors', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                If(
                                    test=Name(id='raise_user_error', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='dummy', ctx=Store()),
                                                        Name(id='errors', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='zip', ctx=Load()),
                                                args=[
                                                    Starred(
                                                        value=Name(id='procurement_errors', ctx=Load()),
                                                        ctx=Load(),
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
                                                        func=Attribute(
                                                            value=Constant(value='\n', kind=None),
                                                            attr='join',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='errors', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ProcurementException', ctx=Load()),
                                                args=[Name(id='procurement_errors', ctx=Load())],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='actions_to_run', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[Name(id='list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='procurement_errors', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='procurement', ctx=Store()),
                            iter=Name(id='procurements', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='company_id', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='procurement', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='priority', kind=None),
                                            Constant(value='0', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                            attr='setdefault',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='date_planned', kind=None),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Datetime',
                                                        ctx=Load(),
                                                    ),
                                                    attr='now',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='procurement', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='consu', kind=None),
                                                            Constant(value='product', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='procurement', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='procurement', ctx=Load()),
                                                                attr='product_uom',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='rule', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_rule',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='procurement', ctx=Load()),
                                                attr='values',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='rule', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='error', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='No rule has been found to replenish "%s" in "%s".\nVerify the routes configuration on the product.', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='procurement', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='procurement', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='procurement_errors', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='procurement', ctx=Load()),
                                                            Name(id='error', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='action', ctx=Store())],
                                            value=IfExp(
                                                test=Compare(
                                                    left=Attribute(
                                                        value=Name(id='rule', ctx=Load()),
                                                        attr='action',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='pull_push', kind=None)],
                                                ),
                                                body=Constant(value='pull', kind=None),
                                                orelse=Attribute(
                                                    value=Name(id='rule', ctx=Load()),
                                                    attr='action',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='actions_to_run', ctx=Load()),
                                                        slice=Name(id='action', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='procurement', ctx=Load()),
                                                            Name(id='rule', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
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
                        If(
                            test=Name(id='procurement_errors', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='raise_exception', ctx=Load()),
                                        args=[Name(id='procurement_errors', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='action', ctx=Store()),
                                    Name(id='procurements', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='actions_to_run', ctx=Load()),
                                    attr='items',
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
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.rule', kind=None),
                                                ctx=Load(),
                                            ),
                                            BinOp(
                                                left=Constant(value='_run_%s', kind=None),
                                                op=Mod(),
                                                right=Name(id='action', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Call(
                                                            func=Name(id='getattr', ctx=Load()),
                                                            args=[
                                                                Subscript(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    slice=Constant(value='stock.rule', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                BinOp(
                                                                    left=Constant(value='_run_%s', kind=None),
                                                                    op=Mod(),
                                                                    right=Name(id='action', ctx=Load()),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        args=[Name(id='procurements', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='ProcurementException', ctx=Load()),
                                                    name='e',
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='procurement_errors', ctx=Store()),
                                                            op=Add(),
                                                            value=Attribute(
                                                                value=Name(id='e', ctx=Load()),
                                                                attr='procurement_exceptions',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[],
                                            finalbody=[],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value="The method _run_%s doesn't exist on the procurement rules", kind=None),
                                                        op=Mod(),
                                                        right=Name(id='action', ctx=Load()),
                                                    ),
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
                        If(
                            test=Name(id='procurement_errors', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Name(id='raise_exception', ctx=Load()),
                                        args=[Name(id='procurement_errors', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
                    name='_search_rule',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='route_ids', annotation=None, type_comment=None),
                            arg(arg='packaging_id', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='warehouse_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' First find a rule among the ones defined on the procurement\n        group, then try on the routes defined for the product, finally fallback\n        on the default behavior\n        ', kind=None),
                        ),
                        If(
                            test=Name(id='warehouse_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='warehouse_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='warehouse_id', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='warehouse_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='domain', ctx=Load()),
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
                            targets=[Name(id='Rule', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.rule', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.rule', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='route_ids', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Rule', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='expression', ctx=Load()),
                                                    attr='AND',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='route_id', kind=None),
                                                                            Constant(value='in', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='route_ids', ctx=Load()),
                                                                                attr='ids',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='domain', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='order',
                                                value=Constant(value='route_sequence, sequence', kind=None),
                                            ),
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
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
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='res', ctx=Load()),
                                    ),
                                    Name(id='packaging_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='packaging_routes', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='packaging_id', ctx=Load()),
                                        attr='route_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='packaging_routes', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Rule', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='expression', ctx=Load()),
                                                            attr='AND',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='route_id', kind=None),
                                                                                    Constant(value='in', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='packaging_routes', ctx=Load()),
                                                                                        attr='ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='domain', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='route_sequence, sequence', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
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
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='res', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product_routes', ctx=Store())],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='product_id', ctx=Load()),
                                            attr='route_ids',
                                            ctx=Load(),
                                        ),
                                        op=BitOr(),
                                        right=Attribute(
                                            value=Attribute(
                                                value=Name(id='product_id', ctx=Load()),
                                                attr='categ_id',
                                                ctx=Load(),
                                            ),
                                            attr='total_route_ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='product_routes', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Rule', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='expression', ctx=Load()),
                                                            attr='AND',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='route_id', kind=None),
                                                                                    Constant(value='in', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='product_routes', ctx=Load()),
                                                                                        attr='ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='domain', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='route_sequence, sequence', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
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
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='res', ctx=Load()),
                                    ),
                                    Name(id='warehouse_id', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='warehouse_routes', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='warehouse_id', ctx=Load()),
                                        attr='route_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='warehouse_routes', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='res', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Rule', ctx=Load()),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='expression', ctx=Load()),
                                                            attr='AND',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value='route_id', kind=None),
                                                                                    Constant(value='in', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='warehouse_routes', ctx=Load()),
                                                                                        attr='ids',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='domain', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='order',
                                                        value=Constant(value='route_sequence, sequence', kind=None),
                                                    ),
                                                    keyword(
                                                        arg='limit',
                                                        value=Constant(value=1, kind=None),
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
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                    name='_get_rule',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Find a pull rule for the location_id, fallback on the parent\n        locations if it could not be found.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='location', ctx=Store())],
                            value=Name(id='location_id', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='result', ctx=Load()),
                                    ),
                                    Name(id='location', ctx=Load()),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_rule_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='location', ctx=Load()),
                                            Name(id='values', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_search_rule',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='route_ids', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='product_packaging_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='product_id', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='values', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='warehouse_id', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='domain', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='location', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                    name='_get_rule_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='location', annotation=None, type_comment=None),
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
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='location_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='location', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='action', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value='push', kind=None),
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
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='su',
                                        ctx=Load(),
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain_company', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='child_of', kind=None),
                                                    Attribute(
                                                        value=Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='ids',
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
                                    targets=[Name(id='domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Name(id='domain', ctx=Load()),
                                                    Name(id='domain_company', ctx=Load()),
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
                            value=Name(id='domain', ctx=Load()),
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
                    name='_get_moves_to_assign_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='moves_domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='confirmed', kind=None),
                                                    Constant(value='partially_available', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='!=', kind=None),
                                            Constant(value=0.0, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='reservation_date', kind=None),
                                            Constant(value='<=', kind=None),
                                            Call(
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
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='company_id', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='moves_domain', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='expression', ctx=Load()),
                                            attr='AND',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='company_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='company_id', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='moves_domain', ctx=Load()),
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
                            value=Name(id='moves_domain', ctx=Load()),
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
                    name='_run_scheduler_tasks',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='use_new_cursor', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
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
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_orderpoint_domain',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='company_id',
                                        value=Name(id='company_id', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='orderpoints', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.warehouse.orderpoint', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='orderpoints', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_compute_qty_to_order',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='use_new_cursor', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='orderpoints', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_procure_orderpoint_confirm',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='use_new_cursor',
                                        value=Name(id='use_new_cursor', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='company_id',
                                        value=Name(id='company_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='raise_user_error',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_moves_to_assign_domain',
                                    ctx=Load(),
                                ),
                                args=[Name(id='company_id', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='moves_to_assign', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=None, kind=None),
                                    ),
                                    keyword(
                                        arg='order',
                                        value=Constant(value='reservation_date, priority desc, date asc, id asc', kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='moves_chunk', ctx=Store()),
                            iter=Call(
                                func=Name(id='split_every', ctx=Load()),
                                args=[
                                    Constant(value=1000, kind=None),
                                    Attribute(
                                        value=Name(id='moves_to_assign', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='moves_chunk', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_action_assign',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='use_new_cursor', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='A batch of %d moves are assigned and committed', kind=None),
                                                    Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='moves_chunk', ctx=Load())],
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
                            orelse=[],
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
                                        slice=Constant(value='stock.quant', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_quant_tasks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Name(id='use_new_cursor', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='commit',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='_logger', ctx=Load()),
                                            attr='info',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='_run_scheduler_tasks is finished and committed', kind=None)],
                                        keywords=[],
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
                FunctionDef(
                    name='run_scheduler',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='use_new_cursor', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
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
                            value=Constant(value=' Call the scheduler in order to check the running procurements (super method), to check the minimum stock rules\n        and the availability of moves. This function is intended to be run for all the companies at the same time, so\n        we run functions as SUPERUSER to avoid intercompanies and access rights issues. ', kind=None),
                        ),
                        Try(
                            body=[
                                If(
                                    test=Name(id='use_new_cursor', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='cr', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Name(id='registry', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_cr',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='dbname',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='cursor',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_env',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='cr',
                                                                value=Name(id='cr', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ],
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='_run_scheduler_tasks',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='use_new_cursor',
                                                value=Name(id='use_new_cursor', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='company_id',
                                                value=Name(id='company_id', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            handlers=[],
                            orelse=[],
                            finalbody=[
                                If(
                                    test=Name(id='use_new_cursor', ctx=Load()),
                                    body=[
                                        Try(
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='_cr',
                                                                ctx=Load(),
                                                            ),
                                                            attr='close',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='Exception', ctx=Load()),
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
                            ],
                        ),
                        Return(
                            value=Dict(keys=[], values=[]),
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
                    name='_get_orderpoint_domain',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='trigger', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='auto', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id.active', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='company_id', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='company_id', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='domain', ctx=Load()),
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
    ],
    type_ignores=[],
)
