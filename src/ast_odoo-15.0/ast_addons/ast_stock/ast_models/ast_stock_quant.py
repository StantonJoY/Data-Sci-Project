Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[
                alias(name='Error', asname=None),
                alias(name='OperationalError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='UserError', asname=None),
                alias(name='ValidationError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
            ],
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
            name='StockQuant',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.quant', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Quants', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='product_id', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_domain_location_id',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_inventory_mode',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='usage', kind=None),
                                            Constant(value='in', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='internal', kind=None),
                                                    Constant(value='transit', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
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
                FunctionDef(
                    name='_domain_lot_id',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_inventory_mode',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value="'|'", kind=None),
                                    Constant(value="('company_id', '=', company_id)", kind=None),
                                    Constant(value="('company_id', '=', False)", kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
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
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='product.product', kind=None)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='domain', ctx=Load()),
                                            attr='insert',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=0, kind=None),
                                            BinOp(
                                                left=Constant(value="('product_id', '=', %s)", kind=None),
                                                op=Mod(),
                                                right=Call(
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
                                                    args=[Constant(value='active_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
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
                                            args=[Constant(value='active_model', kind=None)],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product.template', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='product_template', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='product.template', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
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
                                                        args=[Constant(value='active_id', kind=None)],
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
                                                    value=Name(id='product_template', ctx=Load()),
                                                    attr='exists',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='domain', ctx=Load()),
                                                            attr='insert',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Constant(value=0, kind=None),
                                                            BinOp(
                                                                left=Constant(value="('product_id', 'in', %s)", kind=None),
                                                                op=Mod(),
                                                                right=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='product_template', ctx=Load()),
                                                                        attr='product_variant_ids',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ids',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='domain', ctx=Load()),
                                                    attr='insert',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value="('product_id', '=', product_id)", kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=Constant(value='[', kind=None),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Constant(value=', ', kind=None),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Constant(value=']', kind=None),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_domain_product_id',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_inventory_mode',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='type', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='product', kind=None),
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
                                op=Or(),
                                values=[
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
                                        args=[Constant(value='product_tmpl_ids', kind=None)],
                                        keywords=[],
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
                                        args=[Constant(value='product_tmpl_id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='products', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
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
                                            args=[
                                                Constant(value='product_tmpl_ids', kind=None),
                                                List(elts=[], ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Add(),
                                        right=List(
                                            elts=[
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
                                                    args=[
                                                        Constant(value='product_tmpl_id', kind=None),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='products', ctx=Load()),
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
                        Return(
                            value=Name(id='domain', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='product.product', kind=None),
                            Constant(value='Product', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
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
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_domain_product_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
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
                    targets=[Name(id='product_tmpl_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='product.template', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Product Template', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.product_tmpl_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='uom.uom', kind=None),
                            Constant(value='Unit of Measure', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.uom_id', kind=None),
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
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='location_id.company_id', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                            Constant(value='Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
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
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_domain_location_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
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
                    targets=[Name(id='lot_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.production.lot', kind=None),
                            Constant(value='Lot/Serial Number', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
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
                                    body=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_domain_lot_id',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='package_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.quant.package', kind=None),
                            Constant(value='Package', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('location_id', '=', location_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The package containing this quant', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
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
                    targets=[Name(id='owner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Owner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='This is the owner of the quant', kind=None),
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
                    targets=[Name(id='quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Quantity of products in this quant, in the default unit of measure of the product', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reserved_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reserved Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Quantity of reserved products in this quant, in the default unit of measure of the product', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
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
                    targets=[Name(id='available_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Available Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="On hand quantity which hasn't been reserved on a transfer, in the default unit of measure of the product", kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_available_quantity', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='in_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Incoming Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Datetime',
                                        ctx=Load(),
                                    ),
                                    attr='now',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='tracking', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='product_id.tracking', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='on_hand', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='On Hand', kind=None)],
                        keywords=[
                            keyword(
                                arg='store',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_on_hand', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_categ_id', ctx=Store())],
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
                                value=Constant(value='product_tmpl_id.categ_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inventory_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Counted Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The product's counted quantity.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inventory_quantity_auto_apply', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Inventoried Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_inventory_quantity_auto_apply', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_inventory_quantity', kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='stock.group_stock_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inventory_diff_quantity', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Difference', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_inventory_diff_quantity', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Indicates the gap between the product's theoretical quantity and its counted quantity.", kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inventory_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Scheduled Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_inventory_date', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Next date the On Hand Quantity should be counted.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='inventory_quantity_set', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_inventory_quantity_set', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_outdated', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Quantity has been moved since last count', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_is_outdated', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='Assigned To', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='User assigned to do product count.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_available_quantity',
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
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='available_quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='reserved_quantity',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                Constant(value='quantity', kind=None),
                                Constant(value='reserved_quantity', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_inventory_date',
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
                            targets=[Name(id='quants', ctx=Store())],
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
                                            args=[arg(arg='q', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Attribute(
                                                        value=Name(id='q', ctx=Load()),
                                                        attr='inventory_date',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='q', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='usage',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[In()],
                                                    comparators=[
                                                        List(
                                                            elts=[
                                                                Constant(value='internal', kind=None),
                                                                Constant(value='transit', kind=None),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ],
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
                            targets=[Name(id='date_by_location', ctx=Store())],
                            value=DictComp(
                                key=Name(id='loc', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='loc', ctx=Load()),
                                        attr='_get_next_inventory_date',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='loc', ctx=Store()),
                                        iter=Attribute(
                                            value=Name(id='quants', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='quants', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='date_by_location', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                            args=[Constant(value='location_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_inventory_diff_quantity',
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
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_diff_quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=BinOp(
                                        left=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity',
                                            ctx=Load(),
                                        ),
                                        op=Sub(),
                                        right=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='quantity',
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                            args=[Constant(value='inventory_quantity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_inventory_quantity_set',
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
                                    attr='inventory_quantity_set',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
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
                            args=[Constant(value='inventory_quantity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_is_outdated',
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
                                    attr='is_outdated',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Call(
                                                func=Name(id='float_compare', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='inventory_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='inventory_diff_quantity',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='rounding',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='inventory_quantity_set',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='is_outdated',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
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
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='inventory_quantity', kind=None),
                                Constant(value='quantity', kind=None),
                                Constant(value='product_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_inventory_quantity_auto_apply',
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
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity_auto_apply',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='quant', ctx=Load()),
                                        attr='quantity',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                            args=[Constant(value='quantity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_inventory_quantity',
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
                            value=Constant(value=' Inverse method to create stock move when `inventory_quantity` is set\n        (`inventory_quantity` is only accessible in inventory mode).\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_is_inventory_mode',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='quant', ctx=Load()),
                                        attr='inventory_quantity_auto_apply',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_apply_inventory',
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
                    name='_search_on_hand',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Handle the "on_hand" filter, indirectly calling `_get_domain_locations`.', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Compare(
                                        left=Name(id='operator', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Constant(value='=', kind=None),
                                                    Constant(value='!=', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Name(id='isinstance', ctx=Load()),
                                            args=[
                                                Name(id='value', ctx=Load()),
                                                Name(id='bool', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
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
                                                args=[Constant(value='Operation not supported', kind=None)],
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
                            targets=[Name(id='domain_loc', ctx=Store())],
                            value=Subscript(
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
                                        attr='_get_domain_locations',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='quant_query', ctx=Store())],
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
                                    attr='_search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain_loc', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='!=', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=True, kind=None)],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='operator', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='=', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='value', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='domain_operator', ctx=Store())],
                                    value=Constant(value='not in', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='domain_operator', ctx=Store())],
                                    value=Constant(value='in', kind=None),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Name(id='domain_operator', ctx=Load()),
                                            Name(id='quant_query', ctx=Load()),
                                        ],
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
                FunctionDef(
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to handle the "inventory mode" and create a quant as\n        superuser the conditions are met.\n        ', kind=None),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_inventory_mode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Name(id='f', ctx=Load()),
                                                    ops=[In()],
                                                    comparators=[Name(id='vals', ctx=Load())],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='f', ctx=Store()),
                                                        iter=List(
                                                            elts=[
                                                                Constant(value='inventory_quantity', kind=None),
                                                                Constant(value='inventory_quantity_auto_apply', kind=None),
                                                            ],
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
                            body=[
                                Assign(
                                    targets=[Name(id='allowed_fields', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_inventory_fields_create',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='field', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='field', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='vals', ctx=Load()),
                                                                attr='keys',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='field', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='allowed_fields', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                                        args=[Constant(value="Quant's creation is restricted, you can't do this operation.", kind=None)],
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
                                    targets=[Name(id='inventory_quantity', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='inventory_quantity', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='pop',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='inventory_quantity_auto_apply', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
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
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='product_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='location', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.location', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='vals', ctx=Load()),
                                                slice=Constant(value='location_id', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='lot_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.production.lot', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='lot_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='package_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.quant.package', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='package_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='owner_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='res.partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='owner_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='quant', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_gather',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product', ctx=Load()),
                                            Name(id='location', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lot_id',
                                                value=Name(id='lot_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='package_id',
                                                value=Name(id='package_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='owner_id',
                                                value=Name(id='owner_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='strict',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='quant', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='quant', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='quant', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='quant', ctx=Store())],
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
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='inventory_quantity', ctx=Load()),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='user_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='user_id', kind=None),
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
                                                attr='id',
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
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
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
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='quant', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockQuant', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_is_inventory_mode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='_check_company',
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
                    name='_load_records_create',
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
                        Expr(
                            value=Constant(value=' Add default location if import file did not fill it', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='company_user', ctx=Store())],
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
                            targets=[Name(id='warehouse', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.warehouse', kind=None),
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
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='company_user', ctx=Load()),
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
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='value', ctx=Store()),
                            iter=Name(id='values', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='location_id', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='value', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='location_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='warehouse', ctx=Load()),
                                                    attr='lot_stock_id',
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='_load_records_create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='values', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='read_group',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                            arg(arg='groupby', annotation=None, type_comment=None),
                            arg(arg='offset', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                            arg(arg='orderby', annotation=None, type_comment=None),
                            arg(arg='lazy', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=0, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to set the `inventory_quantity` field if we\'re in "inventory mode" as well\n        as to compute the sum of the `available_quantity` field.\n        ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='available_quantity', kind=None),
                                ops=[In()],
                                comparators=[Name(id='fields', ctx=Load())],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Constant(value='quantity', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='quantity', kind=None)],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='reserved_quantity', kind=None),
                                        ops=[NotIn()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='fields', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='reserved_quantity', kind=None)],
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
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockQuant', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
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
                        For(
                            target=Name(id='group', ctx=Store()),
                            iter=Name(id='result', ctx=Load()),
                            body=[
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
                                        args=[Constant(value='inventory_report_mode', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='inventory_quantity', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Constant(value='available_quantity', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='fields', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='available_quantity', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='quantity', kind=None),
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Subscript(
                                                    value=Name(id='group', ctx=Load()),
                                                    slice=Constant(value='reserved_quantity', kind=None),
                                                    ctx=Load(),
                                                ),
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
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Override to handle the "inventory mode" and create the inventory move. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='allowed_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_inventory_fields_write',
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_is_inventory_mode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='field', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='field', ctx=Store()),
                                                        iter=Name(id='allowed_fields', ctx=Load()),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='field', ctx=Load()),
                                                                ops=[In()],
                                                                comparators=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='vals', ctx=Load()),
                                                                            attr='keys',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Compare(
                                                    left=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='usage',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='inventory', kind=None)],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='quant', ctx=Store()),
                                                        iter=Name(id='self', ctx=Load()),
                                                        ifs=[],
                                                        is_async=0,
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[Return(value=None)],
                                    orelse=[],
                                ),
                                If(
                                    test=Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Name(id='field', ctx=Load()),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='field', ctx=Store()),
                                                        iter=Call(
                                                            func=Attribute(
                                                                value=Name(id='vals', ctx=Load()),
                                                                attr='keys',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        ifs=[
                                                            Compare(
                                                                left=Name(id='field', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='allowed_fields', ctx=Load())],
                                                            ),
                                                        ],
                                                        is_async=0,
                                                    ),
                                                ],
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
                                                        args=[Constant(value="Quant's editing is restricted, you can't do this operation.", kind=None)],
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
                                Assign(
                                    targets=[Name(id='res', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StockQuant', ctx=Load()),
                                                    Name(id='self', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='res', ctx=Load()),
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
                                                args=[Constant(value='inventory_report_mode', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='with_context',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='inventory_report_mode', kind=None)],
                                                                values=[Constant(value=False, kind=None)],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='action_apply_inventory',
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
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='StockQuant', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_stock_moves',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.stock_move_line_action', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='location_id', kind=None),
                                            Constant(value='=', kind=None),
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
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='location_dest_id', kind=None),
                                            Constant(value='=', kind=None),
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
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lot_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='package_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='result_package_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
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
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_quants',
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
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='search_default_internal_loc',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_view_context',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_quants_action',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='extend',
                                        value=Constant(value=True, kind=None),
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
                    name='action_view_inventory',
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
                            value=Constant(value=' Similar to _get_quants_action except specific for inventory adjustments (i.e. inventory counts). ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='self', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_set_view_context',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_quant_tasks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
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
                                    value=Name(id='ctx', ctx=Load()),
                                    slice=Constant(value='no_at_date', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_has_groups',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='stock.group_stock_user', kind=None)],
                                        keywords=[],
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='user_has_groups',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='stock.group_stock_manager', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ctx', ctx=Load()),
                                            slice=Constant(value='search_default_my_count', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='help', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Inventory Adjustments', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='list', kind=None),
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
                                            args=[Constant(value='stock.view_stock_quant_tree_inventory_editable', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='stock.quant', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='ctx', ctx=Load()),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='location_id.usage', kind=None),
                                                    Constant(value='in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='internal', kind=None),
                                                            Constant(value='transit', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='\n                <p class="o_view_nocontent_smiling_face">\n                    Your stock is currently empty\n                </p><p>\n                    Press the CREATE button to define quantity for each product in your stock or import them from a spreadsheet throughout Favorites <span class="fa fa-long-arrow-right"/> Import</p>\n                ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='action', ctx=Load()),
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
                    name='action_apply_inventory',
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
                            targets=[Name(id='products_tracked_without_lot', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='rounding', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='rounding',
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
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Float',
                                                        ctx=Load(),
                                                    ),
                                                    attr='is_zero',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='inventory_diff_quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Name(id='rounding', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Float',
                                                        ctx=Load(),
                                                    ),
                                                    attr='is_zero',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='inventory_quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Name(id='rounding', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='fields', ctx=Load()),
                                                        attr='Float',
                                                        ctx=Load(),
                                                    ),
                                                    attr='is_zero',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Name(id='rounding', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[In()],
                                                comparators=[
                                                    List(
                                                        elts=[
                                                            Constant(value='lot', kind=None),
                                                            Constant(value='serial', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='inventory_quantity',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='quantity',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='products_tracked_without_lot', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
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
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
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
                                    value=Name(id='ctx', ctx=Load()),
                                    slice=Constant(value='default_quant_ids', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='quants_outdated', ctx=Store())],
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
                                            args=[arg(arg='quant', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='is_outdated',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='quants_outdated', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ctx', ctx=Load()),
                                            slice=Constant(value='default_quant_to_fix_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='quants_outdated', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='views', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Conflict in Inventory Adjustment', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Constant(value='form', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='stock.inventory.conflict', kind=None),
                                            Constant(value='new', kind=None),
                                            Name(id='ctx', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='products_tracked_without_lot', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='ctx', ctx=Load()),
                                            slice=Constant(value='default_product_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='products_tracked_without_lot', ctx=Load()),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='views', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Tracked Products in Inventory Adjustment', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Constant(value='form', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='stock.track.confirmation', kind=None),
                                            Constant(value='new', kind=None),
                                            Name(id='ctx', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_apply_inventory',
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
                                    attr='inventory_quantity_set',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_inventory_history',
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='History', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='list,form', kind=None),
                                    Constant(value='stock.move.line', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
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
                                                            args=[Constant(value='stock.view_move_line_tree', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='list', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='search_default_inventory', kind=None),
                                            Constant(value='search_default_done', kind=None),
                                        ],
                                        values=[
                                            Constant(value=1, kind=None),
                                            Constant(value=1, kind=None),
                                        ],
                                    ),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='company_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='|', kind=None),
                                            Tuple(
                                                elts=[
                                                    Constant(value='location_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='location_dest_id', kind=None),
                                                    Constant(value='=', kind=None),
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
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='lot_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='search_default_lot_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='lot_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='package_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='search_default_package_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='package_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='search_default_result_package_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='package_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='owner_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Subscript(
                                                value=Name(id='action', ctx=Load()),
                                                slice=Constant(value='context', kind=None),
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='search_default_owner_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='owner_id',
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
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_set_inventory_quantity',
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
                            targets=[Name(id='quants_already_set', ctx=Store())],
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
                                            args=[arg(arg='quant', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity_set',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='quants_already_set', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='ctx', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='default_quant_ids',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='view', ctx=Store())],
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
                                        args=[
                                            Constant(value='stock.inventory_warning_set_view', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='view_mode', kind=None),
                                            Constant(value='views', kind=None),
                                            Constant(value='view_id', kind=None),
                                            Constant(value='res_model', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='context', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Quantities Already Set', kind=None)],
                                                keywords=[],
                                            ),
                                            Constant(value='ir.actions.act_window', kind=None),
                                            Constant(value='form', kind=None),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Attribute(
                                                                value=Name(id='view', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='view', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='stock.inventory.warning', kind=None),
                                            Constant(value='new', kind=None),
                                            Name(id='ctx', ctx=Load()),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_quantity',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='quant', ctx=Load()),
                                        attr='quantity',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_id',
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
                                    attr='user',
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
                                    attr='inventory_quantity_set',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_reset',
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
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='default_quant_ids',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='view', ctx=Store())],
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
                                args=[
                                    Constant(value='stock.inventory_warning_reset_view', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='views', kind=None),
                                    Constant(value='view_id', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='target', kind=None),
                                    Constant(value='context', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Quantities To Reset', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Constant(value='form', kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Name(id='view', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='form', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='view', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='stock.inventory.warning', kind=None),
                                    Constant(value='new', kind=None),
                                    Name(id='ctx', ctx=Load()),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_set_inventory_quantity_to_zero',
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
                                    attr='inventory_quantity',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inventory_diff_quantity',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='inventory_quantity_set',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_product_id',
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
                        If(
                            test=Call(
                                func=Name(id='any', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Compare(
                                            left=Attribute(
                                                value=Attribute(
                                                    value=Name(id='elem', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='type',
                                                ctx=Load(),
                                            ),
                                            ops=[NotEq()],
                                            comparators=[Constant(value='product', kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='elem', ctx=Store()),
                                                iter=Name(id='self', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValidationError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Quants cannot be created for consumables or services.', kind=None)],
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='product_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_quantity',
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
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='usage',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='inventory', kind=None)],
                                            ),
                                            Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='serial', kind=None)],
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Call(
                                                            func=Name(id='abs', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='quant', ctx=Load()),
                                                                    attr='quantity',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        Constant(value=1, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='quant', ctx=Load()),
                                                                    attr='product_uom_id',
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
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='The serial number has already been assigned: \n Product: %s, Serial Number: %s', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='quant', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='quant', ctx=Load()),
                                                                        attr='lot_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='quantity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_location_id',
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
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            attr='usage',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='view', kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='You cannot take products from or deliver products to a location of type "view" (%s).', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
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
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='location_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_removal_strategy',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='categ_id',
                                    ctx=Load(),
                                ),
                                attr='removal_strategy_id',
                                ctx=Load(),
                            ),
                            body=[
                                Return(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='product_id', ctx=Load()),
                                                attr='categ_id',
                                                ctx=Load(),
                                            ),
                                            attr='removal_strategy_id',
                                            ctx=Load(),
                                        ),
                                        attr='method',
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='loc', ctx=Store())],
                            value=Name(id='location_id', ctx=Load()),
                            type_comment=None,
                        ),
                        While(
                            test=Name(id='loc', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='loc', ctx=Load()),
                                        attr='removal_strategy_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Return(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='loc', ctx=Load()),
                                                    attr='removal_strategy_id',
                                                    ctx=Load(),
                                                ),
                                                attr='method',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='loc', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='loc', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value='fifo', kind=None),
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
                    name='_get_removal_strategy_order',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='removal_strategy', annotation=None, type_comment=None),
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
                                left=Name(id='removal_strategy', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value='fifo', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value='in_date ASC, id', kind=None),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='removal_strategy', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='lifo', kind=None)],
                                    ),
                                    body=[
                                        Return(
                                            value=Constant(value='in_date DESC, id DESC', kind=None),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='removal_strategy', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='closest', kind=None)],
                                            ),
                                            body=[
                                                Return(
                                                    value=Constant(value='location_id ASC, id DESC', kind=None),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='Removal strategy %s not implemented.', kind=None)],
                                            keywords=[],
                                        ),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[Name(id='removal_strategy', ctx=Load())],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
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
                    name='_gather',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='lot_id', annotation=None, type_comment=None),
                            arg(arg='package_id', annotation=None, type_comment=None),
                            arg(arg='owner_id', annotation=None, type_comment=None),
                            arg(arg='strict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='removal_strategy', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_removal_strategy',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='location_id', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='removal_strategy_order', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_removal_strategy_order',
                                    ctx=Load(),
                                ),
                                args=[Name(id='removal_strategy', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='product_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Name(id='product_id', ctx=Load()),
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='strict', ctx=Load()),
                            ),
                            body=[
                                If(
                                    test=Name(id='lot_id', ctx=Load()),
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
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='lot_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='lot_id', ctx=Load()),
                                                                                attr='id',
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
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='package_id', ctx=Load()),
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
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='package_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='package_id', ctx=Load()),
                                                                                attr='id',
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
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='owner_id', ctx=Load()),
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
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value='owner_id', kind=None),
                                                                            Constant(value='=', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='owner_id', ctx=Load()),
                                                                                attr='id',
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
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='location_id', kind=None),
                                                                    Constant(value='child_of', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='location_id', ctx=Load()),
                                                                        attr='id',
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
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
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
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='lot_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='lot_id', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='lot_id', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='package_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='package_id', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='package_id', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='owner_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Name(id='owner_id', ctx=Load()),
                                                                                    Attribute(
                                                                                        value=Name(id='owner_id', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            Constant(value=False, kind=None),
                                                                        ],
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
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='location_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='location_id', ctx=Load()),
                                                                        attr='id',
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
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='order',
                                        value=Name(id='removal_strategy_order', ctx=Load()),
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
                    name='_get_available_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='lot_id', annotation=None, type_comment=None),
                            arg(arg='package_id', annotation=None, type_comment=None),
                            arg(arg='owner_id', annotation=None, type_comment=None),
                            arg(arg='strict', annotation=None, type_comment=None),
                            arg(arg='allow_negative', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Return the available quantity, i.e. the sum of `quantity` minus the sum of\n        `reserved_quantity`, for the set of quants sharing the combination of `product_id,\n        location_id` if `strict` is set to False or sharing the *exact same characteristics*\n        otherwise.\n        This method is called in the following usecases:\n            - when a stock move checks its availability\n            - when a stock move actually assign\n            - when editing a move line, to check if the new value is forced or not\n            - when validating a move line with some forced values and have to potentially unlink an\n              equivalent move line in another picking\n        In the two first usecases, `strict` should be set to `False`, as we don't know what exact\n        quants we'll reserve, and the characteristics are meaningless in this context.\n        In the last ones, `strict` should be set to `True`, as we work on a specific set of\n        characteristics.\n\n        :return: available quantity as a float\n        ", kind=None),
                        ),
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
                        Assign(
                            targets=[Name(id='quants', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_gather',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='location_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lot_id',
                                        value=Name(id='lot_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='package_id',
                                        value=Name(id='package_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='owner_id',
                                        value=Name(id='owner_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='strict',
                                        value=Name(id='strict', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='rounding', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='uom_id',
                                    ctx=Load(),
                                ),
                                attr='rounding',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='tracking',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='none', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='available_quantity', ctx=Store())],
                                    value=BinOp(
                                        left=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='quants', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='quantity', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='quants', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='reserved_quantity', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='allow_negative', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Name(id='available_quantity', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Return(
                                            value=IfExp(
                                                test=Compare(
                                                    left=Call(
                                                        func=Name(id='float_compare', ctx=Load()),
                                                        args=[
                                                            Name(id='available_quantity', ctx=Load()),
                                                            Constant(value=0.0, kind=None),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_rounding',
                                                                value=Name(id='rounding', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    ops=[GtE()],
                                                    comparators=[Constant(value=0.0, kind=None)],
                                                ),
                                                body=Name(id='available_quantity', ctx=Load()),
                                                orelse=Constant(value=0.0, kind=None),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='availaible_quantities', ctx=Store())],
                                    value=DictComp(
                                        key=Name(id='lot_id', ctx=Load()),
                                        value=Constant(value=0.0, kind=None),
                                        generators=[
                                            comprehension(
                                                target=Name(id='lot_id', ctx=Store()),
                                                iter=BinOp(
                                                    left=Call(
                                                        func=Name(id='list', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='set', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='quants', ctx=Load()),
                                                                            attr='mapped',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='lot_id', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    op=Add(),
                                                    right=List(
                                                        elts=[Constant(value='untracked', kind=None)],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='quant', ctx=Store()),
                                    iter=Name(id='quants', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            body=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='availaible_quantities', ctx=Load()),
                                                        slice=Constant(value='untracked', kind=None),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='quantity',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='reserved_quantity',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            orelse=[
                                                AugAssign(
                                                    target=Subscript(
                                                        value=Name(id='availaible_quantities', ctx=Load()),
                                                        slice=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='lot_id',
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Store(),
                                                    ),
                                                    op=Add(),
                                                    value=BinOp(
                                                        left=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='quantity',
                                                            ctx=Load(),
                                                        ),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='reserved_quantity',
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
                                If(
                                    test=Name(id='allow_negative', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='availaible_quantities', ctx=Load()),
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
                                    orelse=[
                                        Return(
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    ListComp(
                                                        elt=Name(id='available_quantity', ctx=Load()),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='available_quantity', ctx=Store()),
                                                                iter=Call(
                                                                    func=Attribute(
                                                                        value=Name(id='availaible_quantities', ctx=Load()),
                                                                        attr='values',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Call(
                                                                            func=Name(id='float_compare', ctx=Load()),
                                                                            args=[
                                                                                Name(id='available_quantity', ctx=Load()),
                                                                                Constant(value=0, kind=None),
                                                                            ],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='precision_rounding',
                                                                                    value=Name(id='rounding', ctx=Load()),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=0, kind=None)],
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
                                    ],
                                ),
                            ],
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
                    name='_onchange_location_or_product_id',
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
                            targets=[Name(id='vals', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lot_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        If(
                                            test=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='tracking',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='none', kind=None)],
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[NotEq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='product_id',
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
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='lot_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='quant', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_gather',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lot_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='package_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='owner_id',
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='owner_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='strict',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='quant', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='quantity',
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
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='serial', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='inventory_quantity', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='inventory_quantity_auto_apply', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='vals', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='vals', ctx=Load())],
                                        keywords=[],
                                    ),
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
                                Constant(value='location_id', kind=None),
                                Constant(value='product_id', kind=None),
                                Constant(value='lot_id', kind=None),
                                Constant(value='package_id', kind=None),
                                Constant(value='owner_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_inventory_quantity',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            attr='usage',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='inventory', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='warning', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='You cannot modify inventory loss quantity', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Editing quantities in an Inventory Adjustment location is forbidden,those locations are used as counterpart when correcting the quantities.', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='warning', kind=None)],
                                        values=[Name(id='warning', ctx=Load())],
                                    ),
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
                            args=[Constant(value='inventory_quantity', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_serial_number',
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
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='lot_id',
                                        ctx=Load(),
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='tracking',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='serial', kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='message', ctx=Store()),
                                                Name(id='dummy', ctx=Store()),
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
                                                slice=Constant(value='stock.quant', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_check_serial_number',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='company_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='message', ctx=Load()),
                                    body=[
                                        Return(
                                            value=Dict(
                                                keys=[Constant(value='warning', kind=None)],
                                                values=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='title', kind=None),
                                                            Constant(value='message', kind=None),
                                                        ],
                                                        values=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Warning', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            Name(id='message', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='lot_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_product_id',
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
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='location_id',
                                ctx=Load(),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    attr='tracking',
                                    ctx=Load(),
                                ),
                                ops=[In()],
                                comparators=[
                                    List(
                                        elts=[
                                            Constant(value='lot', kind=None),
                                            Constant(value='serial', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='previous_quants', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='location_id.usage', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='internal', kind=None),
                                                                    Constant(value='transit', kind=None),
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
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                            keyword(
                                                arg='order',
                                                value=Constant(value='create_date desc', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='previous_quants', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='previous_quants', ctx=Load()),
                                                attr='location_id',
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
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='location_id',
                                    ctx=Load(),
                                ),
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
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='company_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
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
                                        ],
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
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.warehouse', kind=None),
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
                                                                    Constant(value='company_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Name(id='company_id', ctx=Load()),
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
                                            attr='in_type_id',
                                            ctx=Load(),
                                        ),
                                        attr='default_location_dest_id',
                                        ctx=Load(),
                                    ),
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
                                Constant(value='product_id', kind=None),
                                Constant(value='company_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_apply_inventory',
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
                            targets=[Name(id='move_vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='stock.group_stock_manager', kind=None)],
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
                                                args=[Constant(value='Only a stock manager can validate an inventory adjustment.', kind=None)],
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
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='inventory_diff_quantity',
                                                    ctx=Load(),
                                                ),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='product_uom_id',
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move_vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='_get_inventory_move_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='inventory_diff_quantity',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='with_company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='property_stock_inventory',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='location_id',
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
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='move_vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='_get_inventory_move_values',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Attribute(
                                                                    value=Name(id='quant', ctx=Load()),
                                                                    attr='inventory_diff_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='quant', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Call(
                                                                    func=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='with_company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(id='quant', ctx=Load()),
                                                                            attr='company_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                                attr='property_stock_inventory',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='out',
                                                                value=Constant(value=True, kind=None),
                                                            ),
                                                        ],
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
                        Assign(
                            targets=[Name(id='moves', ctx=Store())],
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
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='inventory_mode',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='move_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='moves', ctx=Load()),
                                    attr='_action_done',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='location_id',
                                        ctx=Load(),
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='last_inventory_date', kind=None)],
                                        values=[
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
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='date_by_location', ctx=Store())],
                            value=DictComp(
                                key=Name(id='loc', ctx=Load()),
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='loc', ctx=Load()),
                                        attr='_get_next_inventory_date',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='loc', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='location_id', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='inventory_date',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='date_by_location', ctx=Load()),
                                        slice=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='location_id',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='inventory_quantity', kind=None),
                                            Constant(value='user_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0, kind=None),
                                            Constant(value=False, kind=None),
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='inventory_diff_quantity', kind=None)],
                                        values=[Constant(value=0, kind=None)],
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
                    name='_update_available_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='lot_id', annotation=None, type_comment=None),
                            arg(arg='package_id', annotation=None, type_comment=None),
                            arg(arg='owner_id', annotation=None, type_comment=None),
                            arg(arg='in_date', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Increase or decrease `reserved_quantity` of a set of quants for a given set of\n        product_id/location_id/lot_id/package_id/owner_id.\n\n        :param product_id:\n        :param location_id:\n        :param quantity:\n        :param lot_id:\n        :param package_id:\n        :param owner_id:\n        :param datetime in_date: Should only be passed when calls to this method are done in\n                                 order to move a quant. When creating a tracked quant, the\n                                 current datetime will be used.\n        :return: tuple (available_quantity, in_date as a datetime)\n        ', kind=None),
                        ),
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
                        Assign(
                            targets=[Name(id='quants', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_gather',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='location_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lot_id',
                                        value=Name(id='lot_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='package_id',
                                        value=Name(id='package_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='owner_id',
                                        value=Name(id='owner_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='strict',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='incoming_dates', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='d', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='d', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='quants', ctx=Load()),
                                                attr='mapped',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='in_date', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[Name(id='d', ctx=Load())],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='in_date', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='incoming_dates', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[Name(id='in_date', ctx=Load())],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='incoming_dates', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='in_date', ctx=Store())],
                                    value=Call(
                                        func=Name(id='min', ctx=Load()),
                                        args=[Name(id='incoming_dates', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='in_date', ctx=Store())],
                                    value=Call(
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
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='quant', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='quants', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='SELECT id FROM stock_quant WHERE id IN %s LIMIT 1 FOR NO KEY UPDATE SKIP LOCKED', kind=None),
                                            List(
                                                elts=[
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='quants', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='stock_quant_result', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='fetchone',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='stock_quant_result', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='quant', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='stock_quant_result', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
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
                            test=Name(id='quant', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='quant', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='in_date', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Attribute(
                                                            value=Name(id='quant', ctx=Load()),
                                                            attr='quantity',
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='quantity', ctx=Load()),
                                                    ),
                                                    Name(id='in_date', ctx=Load()),
                                                ],
                                            ),
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='location_id', kind=None),
                                                    Constant(value='quantity', kind=None),
                                                    Constant(value='lot_id', kind=None),
                                                    Constant(value='package_id', kind=None),
                                                    Constant(value='owner_id', kind=None),
                                                    Constant(value='in_date', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='product_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='location_id', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='quantity', ctx=Load()),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='lot_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='lot_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='package_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='package_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='owner_id', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='owner_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Name(id='in_date', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_available_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product_id', ctx=Load()),
                                            Name(id='location_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lot_id',
                                                value=Name(id='lot_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='package_id',
                                                value=Name(id='package_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='owner_id',
                                                value=Name(id='owner_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='strict',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='allow_negative',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    Name(id='in_date', ctx=Load()),
                                ],
                                ctx=Load(),
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
                    name='_update_reserved_quantity',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='lot_id', annotation=None, type_comment=None),
                            arg(arg='package_id', annotation=None, type_comment=None),
                            arg(arg='owner_id', annotation=None, type_comment=None),
                            arg(arg='strict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Increase the reserved quantity, i.e. increase `reserved_quantity` for the set of quants\n        sharing the combination of `product_id, location_id` if `strict` is set to False or sharing\n        the *exact same characteristics* otherwise. Typically, this method is called when reserving\n        a move or updating a reserved move line. When reserving a chained move, the strict flag\n        should be enabled (to reserve exactly what was brought). When the move is MTS,it could take\n        anything from the stock, so we disable the flag. When editing a move line, we naturally\n        enable the flag, to reflect the reservation according to the edition.\n\n        :return: a list of tuples (quant, quantity_reserved) showing on which quant the reservation\n            was done and how much the system was able to reserve on it\n        ', kind=None),
                        ),
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
                        Assign(
                            targets=[Name(id='rounding', ctx=Store())],
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='uom_id',
                                    ctx=Load(),
                                ),
                                attr='rounding',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='quants', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_gather',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='product_id', ctx=Load()),
                                    Name(id='location_id', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='lot_id',
                                        value=Name(id='lot_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='package_id',
                                        value=Name(id='package_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='owner_id',
                                        value=Name(id='owner_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='strict',
                                        value=Name(id='strict', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='reserved_quants', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Call(
                                    func=Name(id='float_compare', ctx=Load()),
                                    args=[
                                        Name(id='quantity', ctx=Load()),
                                        Constant(value=0, kind=None),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='precision_rounding',
                                            value=Name(id='rounding', ctx=Load()),
                                        ),
                                    ],
                                ),
                                ops=[Gt()],
                                comparators=[Constant(value=0, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='available_quantity', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_available_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='product_id', ctx=Load()),
                                            Name(id='location_id', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='lot_id',
                                                value=Name(id='lot_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='package_id',
                                                value=Name(id='package_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='owner_id',
                                                value=Name(id='owner_id', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='strict',
                                                value=Name(id='strict', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='quantity', ctx=Load()),
                                                Name(id='available_quantity', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Name(id='rounding', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='It is not possible to reserve more products of %s than you have in stock.', kind=None),
                                                            Attribute(
                                                                value=Name(id='product_id', ctx=Load()),
                                                                attr='display_name',
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
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='quantity', ctx=Load()),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Name(id='rounding', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[Lt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='available_quantity', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sum', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='quants', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='reserved_quantity', kind=None)],
                                                        keywords=[],
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
                                                        Call(
                                                            func=Name(id='abs', ctx=Load()),
                                                            args=[Name(id='quantity', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        Name(id='available_quantity', ctx=Load()),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Name(id='rounding', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                ops=[Gt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[
                                                                    Constant(value='It is not possible to unreserve more products of %s than you have in stock.', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='product_id', ctx=Load()),
                                                                        attr='display_name',
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
                                    ],
                                    orelse=[
                                        Return(
                                            value=Name(id='reserved_quants', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        For(
                            target=Name(id='quant', ctx=Store()),
                            iter=Name(id='quants', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='float_compare', ctx=Load()),
                                            args=[
                                                Name(id='quantity', ctx=Load()),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_rounding',
                                                    value=Name(id='rounding', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='max_quantity_on_quant', ctx=Store())],
                                            value=BinOp(
                                                left=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='quantity',
                                                    ctx=Load(),
                                                ),
                                                op=Sub(),
                                                right=Attribute(
                                                    value=Name(id='quant', ctx=Load()),
                                                    attr='reserved_quantity',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Name(id='max_quantity_on_quant', ctx=Load()),
                                                        Constant(value=0, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Name(id='rounding', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                                ops=[LtE()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='max_quantity_on_quant', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Name(id='max_quantity_on_quant', ctx=Load()),
                                                    Name(id='quantity', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='reserved_quantity',
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='reserved_quants', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='quant', ctx=Load()),
                                                            Name(id='max_quantity_on_quant', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='quantity', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='available_quantity', ctx=Store()),
                                            op=Sub(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='max_quantity_on_quant', ctx=Store())],
                                            value=Call(
                                                func=Name(id='min', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='quant', ctx=Load()),
                                                        attr='reserved_quantity',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='abs', ctx=Load()),
                                                        args=[Name(id='quantity', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        AugAssign(
                                            target=Attribute(
                                                value=Name(id='quant', ctx=Load()),
                                                attr='reserved_quantity',
                                                ctx=Store(),
                                            ),
                                            op=Sub(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='reserved_quants', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Name(id='quant', ctx=Load()),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='max_quantity_on_quant', ctx=Load()),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        AugAssign(
                                            target=Name(id='quantity', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                        AugAssign(
                                            target=Name(id='available_quantity', ctx=Store()),
                                            op=Add(),
                                            value=Name(id='max_quantity_on_quant', ctx=Load()),
                                        ),
                                    ],
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='quantity', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Name(id='rounding', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                            Call(
                                                func=Name(id='float_is_zero', ctx=Load()),
                                                args=[Name(id='available_quantity', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='precision_rounding',
                                                        value=Name(id='rounding', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[Break()],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='reserved_quants', ctx=Load()),
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
                    name='_unlink_zero_quants',
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
                            value=Constant(value=' _update_available_quantity may leave quants with no\n        quantity and no reserved_quantity. It used to directly unlink\n        these zero quants but this proved to hurt the performance as\n        this method is often called in batch and each unlink invalidate\n        the cache. We defer the calls to unlink in this method.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='precision_digits', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Constant(value=6, kind=None),
                                    BinOp(
                                        left=Attribute(
                                            value=Call(
                                                func=Attribute(
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
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='ref',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='product.decimal_product_uom', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='digits',
                                            ctx=Load(),
                                        ),
                                        op=Mult(),
                                        right=Constant(value=2, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='SELECT id FROM stock_quant WHERE (round(quantity::numeric, %s) = 0 OR quantity IS NULL)\n                                                     AND round(reserved_quantity::numeric, %s) = 0\n                                                     AND (round(inventory_quantity::numeric, %s) = 0 OR inventory_quantity IS NULL)\n                                                     AND user_id IS NULL;', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='params', ctx=Store())],
                            value=Tuple(
                                elts=[
                                    Name(id='precision_digits', ctx=Load()),
                                    Name(id='precision_digits', ctx=Load()),
                                    Name(id='precision_digits', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='cr',
                                        ctx=Load(),
                                    ),
                                    attr='execute',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='query', ctx=Load()),
                                    Name(id='params', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='quant_ids', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    ListComp(
                                        elt=Subscript(
                                            value=Name(id='quant', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='quant', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            attr='cr',
                                                            ctx=Load(),
                                                        ),
                                                        attr='dictfetchall',
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
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='quant_ids', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_merge_quants',
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
                            value=Constant(value=' In a situation where one transaction is updating a quant via\n        `_update_available_quantity` and another concurrent one calls this function with the same\n        argument, we’ll create a new quant in order for these transactions to not rollback. This\n        method will find and deduplicate these quants.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='query', ctx=Store())],
                            value=Constant(value='WITH\n                        dupes AS (\n                            SELECT min(id) as to_update_quant_id,\n                                (array_agg(id ORDER BY id))[2:array_length(array_agg(id), 1)] as to_delete_quant_ids,\n                                SUM(reserved_quantity) as reserved_quantity,\n                                SUM(inventory_quantity) as inventory_quantity,\n                                SUM(quantity) as quantity,\n                                MIN(in_date) as in_date\n                            FROM stock_quant\n                            GROUP BY product_id, company_id, location_id, lot_id, package_id, owner_id\n                            HAVING count(id) > 1\n                        ),\n                        _up AS (\n                            UPDATE stock_quant q\n                                SET quantity = d.quantity,\n                                    reserved_quantity = d.reserved_quantity,\n                                    inventory_quantity = d.inventory_quantity,\n                                    in_date = d.in_date\n                            FROM dupes d\n                            WHERE d.to_update_quant_id = q.id\n                        )\n                   DELETE FROM stock_quant WHERE id in (SELECT unnest(to_delete_quant_ids) from dupes)\n        ', kind=None),
                            type_comment=None,
                        ),
                        Try(
                            body=[
                                With(
                                    items=[
                                        withitem(
                                            context_expr=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='savepoint',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            optional_vars=None,
                                        ),
                                    ],
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='execute',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='query', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='invalidate_cache',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Name(id='Error', ctx=Load()),
                                    name='e',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='info',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='an error occured while merging quants: %s', kind=None),
                                                    Attribute(
                                                        value=Name(id='e', ctx=Load()),
                                                        attr='pgerror',
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
                            finalbody=[],
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
                    name='_quant_tasks',
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
                                    attr='_merge_quants',
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
                                    attr='_unlink_zero_quants',
                                    ctx=Load(),
                                ),
                                args=[],
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
                    name='_is_inventory_mode',
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
                            value=Constant(value=' Used to control whether a quant was written on or created during an\n        "inventory session", meaning a mode where we need to create the stock.move\n        record necessary to be consistent with the `inventory_quantity` field.\n        ', kind=None),
                        ),
                        Return(
                            value=BoolOp(
                                op=And(),
                                values=[
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
                                        args=[Constant(value='inventory_mode', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_has_groups',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='stock.group_stock_user', kind=None)],
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
                    name='_get_inventory_fields_create',
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
                            value=Constant(value=' Returns a list of fields user can edit when he want to create a quant in `inventory_mode`.\n        ', kind=None),
                        ),
                        Return(
                            value=BinOp(
                                left=List(
                                    elts=[
                                        Constant(value='product_id', kind=None),
                                        Constant(value='location_id', kind=None),
                                        Constant(value='lot_id', kind=None),
                                        Constant(value='package_id', kind=None),
                                        Constant(value='owner_id', kind=None),
                                    ],
                                    ctx=Load(),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_get_inventory_fields_write',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
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
                    name='_get_inventory_fields_write',
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
                            value=Constant(value=' Returns a list of fields user can edit when he want to edit a quant in `inventory_mode`.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='inventory_quantity', kind=None),
                                    Constant(value='inventory_quantity_auto_apply', kind=None),
                                    Constant(value='inventory_diff_quantity', kind=None),
                                    Constant(value='inventory_date', kind=None),
                                    Constant(value='user_id', kind=None),
                                    Constant(value='inventory_quantity_set', kind=None),
                                    Constant(value='is_outdated', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='fields', ctx=Load()),
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
                    name='_get_inventory_move_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='qty', annotation=None, type_comment=None),
                            arg(arg='location_id', annotation=None, type_comment=None),
                            arg(arg='location_dest_id', annotation=None, type_comment=None),
                            arg(arg='out', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Called when user manually set a new quantity (via `inventory_quantity`)\n        just before creating the corresponding stock move.\n\n        :param location_id: `stock.location`\n        :param location_dest_id: `stock.location`\n        :param out: boolean to set on True when the move go to inventory adjustment location.\n        :return: dict with all values needed to create a new `stock.move` with its move line.\n        ', kind=None),
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
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Float',
                                        ctx=Load(),
                                    ),
                                    attr='is_zero',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='qty', ctx=Load()),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='precision_rounding',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='rounding',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Product Quantity Confirmed', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Product Quantity Updated', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='product_id', kind=None),
                                    Constant(value='product_uom', kind=None),
                                    Constant(value='product_uom_qty', kind=None),
                                    Constant(value='company_id', kind=None),
                                    Constant(value='state', kind=None),
                                    Constant(value='location_id', kind=None),
                                    Constant(value='location_dest_id', kind=None),
                                    Constant(value='is_inventory', kind=None),
                                    Constant(value='move_line_ids', kind=None),
                                ],
                                values=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
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
                                                args=[Constant(value='inventory_name', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='name', ctx=Load()),
                                        ],
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Name(id='qty', ctx=Load()),
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
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Constant(value='confirmed', kind=None),
                                    Attribute(
                                        value=Name(id='location_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='location_dest_id', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value=True, kind=None),
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value=0, kind=None),
                                                    Constant(value=0, kind=None),
                                                    Dict(
                                                        keys=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='product_uom_id', kind=None),
                                                            Constant(value='qty_done', kind=None),
                                                            Constant(value='location_id', kind=None),
                                                            Constant(value='location_dest_id', kind=None),
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='lot_id', kind=None),
                                                            Constant(value='package_id', kind=None),
                                                            Constant(value='result_package_id', kind=None),
                                                            Constant(value='owner_id', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='qty', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='location_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='location_dest_id', ctx=Load()),
                                                                attr='id',
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
                                                                                attr='env',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='company',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Name(id='out', ctx=Load()),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=Or(),
                                                                values=[
                                                                    BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Name(id='out', ctx=Load()),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='owner_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
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
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_view_context',
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
                            value=Constant(value=' Adds context when opening quants related views. ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='user_has_groups',
                                        ctx=Load(),
                                    ),
                                    args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='company_user', ctx=Store())],
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
                                    targets=[Name(id='warehouse', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.warehouse', kind=None),
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
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company_user', ctx=Load()),
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
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='warehouse', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='self', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='default_location_id',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='warehouse', ctx=Load()),
                                                                attr='lot_stock_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='hide_location',
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
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='user_has_groups',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.group_stock_user', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='self', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='inventory_mode',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='self', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_quants_action',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='domain', annotation=None, type_comment=None),
                            arg(arg='extend', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns an action to open (non-inventory adjustment) quant view.\n        Depending of the context (user have right to be inventory mode or not),\n        the list view will be editable or readonly.\n\n        :param domain: List for the domain, empty by default.\n        :param extend: If True, enables form, graph and pivot views. False by default.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_quant_tasks',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ctx', ctx=Store())],
                            value=Call(
                                func=Name(id='dict', ctx=Load()),
                                args=[
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            Dict(keys=[], values=[]),
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
                                    value=Name(id='ctx', ctx=Load()),
                                    slice=Constant(value='inventory_report_mode', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ctx', ctx=Load()),
                                    attr='pop',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='group_by', kind=None),
                                    Constant(value=None, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='action', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='name', kind=None),
                                    Constant(value='view_type', kind=None),
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='type', kind=None),
                                    Constant(value='context', kind=None),
                                    Constant(value='domain', kind=None),
                                    Constant(value='help', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Stock On Hand', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='tree', kind=None),
                                    Constant(value='list,form', kind=None),
                                    Constant(value='stock.quant', kind=None),
                                    Constant(value='ir.actions.act_window', kind=None),
                                    Name(id='ctx', ctx=Load()),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='domain', ctx=Load()),
                                            List(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    Constant(value='\n                <p class="o_view_nocontent_empty_folder">No Stock On Hand</p>\n                <p>This analysis gives you an overview of the current stock\n                level of your products.</p>\n                ', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='target_action', ctx=Store())],
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
                                args=[
                                    Constant(value='stock.dashboard_open_quants', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='target_action', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='target_action', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='form_view', ctx=Store())],
                            value=Attribute(
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
                                    args=[Constant(value='stock.view_stock_quant_form_editable', kind=None)],
                                    keywords=[],
                                ),
                                attr='id',
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
                                        args=[Constant(value='inventory_mode', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='user_has_groups',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='stock.group_stock_manager', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='view_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                            args=[Constant(value='stock.view_stock_quant_tree_editable', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='action', ctx=Load()),
                                            slice=Constant(value='view_id', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                            args=[Constant(value='stock.view_stock_quant_tree', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='action', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='views', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='action', ctx=Load()),
                                                                slice=Constant(value='view_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='list', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Name(id='form_view', ctx=Load()),
                                                            Constant(value='form', kind=None),
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
                        If(
                            test=Name(id='extend', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='action', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='view_mode', kind=None),
                                                    Constant(value='views', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='tree,form,pivot,graph', kind=None),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='action', ctx=Load()),
                                                                        slice=Constant(value='view_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='list', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Name(id='form_view', ctx=Load()),
                                                                    Constant(value='form', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
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
                                                                            args=[Constant(value='stock.view_stock_quant_pivot', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='pivot', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
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
                                                                            args=[Constant(value='stock.stock_quant_view_graph', kind=None)],
                                                                            keywords=[],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Constant(value='graph', kind=None),
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
                            value=Name(id='action', ctx=Load()),
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
                    name='_check_serial_number',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_id', annotation=None, type_comment=None),
                            arg(arg='lot_id', annotation=None, type_comment=None),
                            arg(arg='company_id', annotation=None, type_comment=None),
                            arg(arg='source_location_id', annotation=None, type_comment=None),
                            arg(arg='ref_doc_location_id', annotation=None, type_comment=None),
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
                        Expr(
                            value=Constant(value=' Checks for duplicate serial numbers (SN) when assigning a SN (i.e. no source_location_id)\n        and checks for potential incorrect location selection of a SN when using a SN (i.e.\n        source_location_id). Returns warning message of all locations the SN is located at and\n        (optionally) a recommended source location of the SN (when using SN from incorrect location).\n        This function is designed to be used by onchange functions across differing situations including,\n        but not limited to scrap, incoming picking SN encoding, and outgoing picking SN selection.\n\n        :param product_id: `product.product` product to check SN for\n        :param lot_id: `stock.production.lot` SN to check\n        :param company_id: `res.company` company to check against (i.e. we ignore duplicate SNs across\n            different companies)\n        :param source_location_id: `stock.location` optional source location if using the SN rather\n            than assigning it\n        :param ref_doc_location_id: `stock.location` optional reference document location for\n            determining recommended location. This is param expected to only be used when a\n            `source_location_id` is provided.\n        :return: tuple(message, recommended_location) If not None, message is a string expected to be\n            used in warning message dict and recommended_location is a `location_id`\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='recommended_location', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='product_id', ctx=Load()),
                                    attr='tracking',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='serial', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='quants', ctx=Store())],
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='product_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='lot_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='lot_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='quantity', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=0, kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='|', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='location_id.usage', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='customer', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='&', kind=None),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='company_id', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='location_id.usage', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='internal', kind=None),
                                                                    Constant(value='transit', kind=None),
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
                                    targets=[Name(id='sn_locations', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='quants', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='location_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='quants', ctx=Load()),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='source_location_id', ctx=Load()),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='The Serial Number (%s) is already used in these location(s): %s.\n\nIs this expected? For example this can occur if a delivery operation is validated before its corresponding receipt operation is validated. In this case the issue will be solved automatically once all steps are completed. Otherwise, the serial number should be corrected to prevent inconsistent data.', kind=None),
                                                            Attribute(
                                                                value=Name(id='lot_id', ctx=Load()),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            Call(
                                                                func=Attribute(
                                                                    value=Constant(value=', ', kind=None),
                                                                    attr='join',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='sn_locations', ctx=Load()),
                                                                            attr='mapped',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='display_name', kind=None)],
                                                                        keywords=[],
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
                                            orelse=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Name(id='source_location_id', ctx=Load()),
                                                            Compare(
                                                                left=Name(id='source_location_id', ctx=Load()),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='sn_locations', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='recommended_location', ctx=Store())],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='stock.location', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='ref_doc_location_id', ctx=Load()),
                                                            body=[
                                                                For(
                                                                    target=Name(id='location', ctx=Store()),
                                                                    iter=Name(id='sn_locations', ctx=Load()),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='ref_doc_location_id', ctx=Load()),
                                                                                    attr='parent_path',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[In()],
                                                                                comparators=[
                                                                                    Attribute(
                                                                                        value=Name(id='location', ctx=Load()),
                                                                                        attr='parent_path',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='recommended_location', ctx=Store())],
                                                                                    value=Name(id='location', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Break(),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                For(
                                                                    target=Name(id='location', ctx=Store()),
                                                                    iter=Name(id='sn_locations', ctx=Load()),
                                                                    body=[
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='location', ctx=Load()),
                                                                                    attr='usage',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[NotEq()],
                                                                                comparators=[Constant(value='customer', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='recommended_location', ctx=Store())],
                                                                                    value=Name(id='location', ctx=Load()),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Break(),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                        If(
                                                            test=Name(id='recommended_location', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='Serial number (%s) is not located in %s, but is located in location(s): %s.\n\nSource location for this move will be changed to %s', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='lot_id', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='source_location_id', ctx=Load()),
                                                                                attr='display_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value=', ', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='sn_locations', ctx=Load()),
                                                                                            attr='mapped',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='display_name', kind=None)],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='recommended_location', ctx=Load()),
                                                                                attr='display_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[
                                                                            Constant(value='Serial number (%s) is not located in %s, but is located in location(s): %s.\n\nPlease correct this to prevent inconsistent data.', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='lot_id', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='source_location_id', ctx=Load()),
                                                                                attr='display_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value=', ', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='sn_locations', ctx=Load()),
                                                                                            attr='mapped',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Constant(value='display_name', kind=None)],
                                                                                        keywords=[],
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
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='message', ctx=Load()),
                                    Name(id='recommended_location', ctx=Load()),
                                ],
                                ctx=Load(),
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
            name='QuantPackage',
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
                    value=Constant(value=' Packages containing quants and/or other packages ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='stock.quant.package', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Packages', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='name', kind=None),
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
                        args=[Constant(value='Package Reference', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
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
                                                args=[Constant(value='stock.quant.package', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Unknown Pack', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='quant_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='One2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.quant', kind=None),
                            Constant(value='package_id', kind=None),
                            Constant(value='Bulk Content', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=List(
                                    elts=[
                                        Constant(value='|', kind=None),
                                        Tuple(
                                            elts=[
                                                Constant(value='quantity', kind=None),
                                                Constant(value='!=', kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                        Tuple(
                                            elts=[
                                                Constant(value='reserved_quantity', kind=None),
                                                Constant(value='!=', kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='package_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.package.type', kind=None),
                            Constant(value='Package Type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='index',
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
                    targets=[Name(id='location_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='Location', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_package_info', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
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
                                arg='compute',
                                value=Constant(value='_compute_package_info', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='owner_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.partner', kind=None),
                            Constant(value='Owner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_package_info', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_owner', kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
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
                    targets=[Name(id='package_use', ctx=Store())],
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
                                            Constant(value='disposable', kind=None),
                                            Constant(value='Disposable Box', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='reusable', kind=None),
                                            Constant(value='Reusable Box', kind=None),
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
                                value=Constant(value='Package Use', kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='disposable', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Reusable boxes are used for batch picking and emptied afterwards to be reused. In the barcode application, scanning a reusable box will add the products in this box.\n        Disposable boxes aren't reused, when scanning a disposable box in the barcode application, the contained products are added to the transfer.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_package_info',
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
                            target=Name(id='package', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='values', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='location_id', kind=None),
                                            Constant(value='owner_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='package', ctx=Load()),
                                        attr='quant_ids',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='values', ctx=Load()),
                                                    slice=Constant(value='location_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='package', ctx=Load()),
                                                        attr='quant_ids',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value=0, kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Attribute(
                                                                value=Name(id='q', ctx=Load()),
                                                                attr='owner_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='package', ctx=Load()),
                                                                            attr='quant_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='owner_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='q', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='package', ctx=Load()),
                                                                    attr='quant_ids',
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
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='owner_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='quant_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='owner_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=Call(
                                                func=Name(id='all', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Attribute(
                                                                value=Name(id='q', ctx=Load()),
                                                                attr='company_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='package', ctx=Load()),
                                                                            attr='quant_ids',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='q', ctx=Store()),
                                                                iter=Attribute(
                                                                    value=Name(id='package', ctx=Load()),
                                                                    attr='quant_ids',
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
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='values', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='quant_ids',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value=0, kind=None),
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
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='location_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='location_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='company_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='values', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='company_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='package', ctx=Load()),
                                            attr='owner_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Name(id='values', ctx=Load()),
                                        slice=Constant(value='owner_id', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
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
                                Constant(value='quant_ids.package_id', kind=None),
                                Constant(value='quant_ids.location_id', kind=None),
                                Constant(value='quant_ids.company_id', kind=None),
                                Constant(value='quant_ids.owner_id', kind=None),
                                Constant(value='quant_ids.quantity', kind=None),
                                Constant(value='quant_ids.reserved_quantity', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_owner',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
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
                            test=Name(id='value', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='packs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='quant_ids.owner_id', kind=None),
                                                            Name(id='operator', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
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
                            orelse=[
                                Assign(
                                    targets=[Name(id='packs', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='quant_ids', kind=None),
                                                            Name(id='operator', ctx=Load()),
                                                            Name(id='value', ctx=Load()),
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
                        ),
                        If(
                            test=Name(id='packs', ctx=Load()),
                            body=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='parent_of', kind=None),
                                                    Attribute(
                                                        value=Name(id='packs', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[
                                Return(
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value=False, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unpack',
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
                            target=Name(id='package', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='move_line_to_modify', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='stock.move.line', kind=None),
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
                                                            Constant(value='package_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='package', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='state', kind=None),
                                                            Constant(value='in', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='assigned', kind=None),
                                                                    Constant(value='partially_available', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='product_qty', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Constant(value=0, kind=None),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_line_to_modify', ctx=Load()),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='package_id', kind=None)],
                                                values=[Constant(value=False, kind=None)],
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
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='package', ctx=Load()),
                                                            attr='mapped',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='quant_ids', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='write',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[Constant(value='package_id', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_view_picking',
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
                            targets=[Name(id='action', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.actions.actions', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_for_xml_id',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='stock.action_picking_tree_all', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='|', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='result_package_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='package_id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
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
                            targets=[Name(id='pickings', ctx=Store())],
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
                                                slice=Constant(value='stock.move.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='picking_id', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='action', ctx=Load()),
                                    slice=Constant(value='domain', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='id', kind=None),
                                            Constant(value='in', kind=None),
                                            Attribute(
                                                value=Name(id='pickings', ctx=Load()),
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
                        Return(
                            value=Name(id='action', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_contained_quants',
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
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='package_id', kind=None),
                                                    Constant(value='in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
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
