Module(
    body=[
        ImportFrom(
            module='collections',
            names=[
                alias(name='Counter', asname=None),
                alias(name='defaultdict', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='tools', asname=None),
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
            module='odoo.tools',
            names=[alias(name='OrderedSet', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.float_utils',
            names=[
                alias(name='float_compare', asname=None),
                alias(name='float_is_zero', asname=None),
                alias(name='float_round', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_model',
            names=[alias(name='MODULE_UNINSTALL_FLAG', asname=None)],
            level=0,
        ),
        ClassDef(
            name='StockMoveLine',
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
                    value=Constant(value='stock.move.line', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Product Moves (Stock Move Line)', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='product_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='result_package_id desc, location_id asc, location_dest_id asc, picking_id asc, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking', kind=None),
                            Constant(value='Transfer', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The stock operation where the packing has been made', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='move_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move', kind=None),
                            Constant(value='Stock Move', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Change to a better name', kind=None),
                            ),
                            keyword(
                                arg='index',
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
                        args=[Constant(value='res.company', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Company', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
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
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('type', '!=', 'service'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]", kind=None),
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
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('category_id', '=', product_uom_category_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_uom_category_id', ctx=Store())],
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
                                value=Constant(value='product_id.uom_id.category_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='product_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Real Reserved Quantity', kind=None)],
                        keywords=[
                            keyword(
                                arg='digits',
                                value=Constant(value=0, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_product_qty', kind=None),
                            ),
                            keyword(
                                arg='inverse',
                                value=Constant(value='_set_product_qty', kind=None),
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
                    targets=[Name(id='product_uom_qty', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Reserved', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='qty_done', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Done', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=0.0, kind=None),
                            ),
                            keyword(
                                arg='digits',
                                value=Constant(value='Product Unit of Measure', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
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
                            Constant(value='Source Package', kind=None),
                        ],
                        keywords=[
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
                                value=Constant(value="[('location_id', '=', location_id)]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='package_level_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.package_level', kind=None),
                            Constant(value='Package Level', kind=None),
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
                                arg='domain',
                                value=Constant(value="[('product_id', '=', product_id), ('company_id', '=', company_id)]", kind=None),
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
                    targets=[Name(id='lot_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Lot/Serial Number Name', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='result_package_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.quant.package', kind=None),
                            Constant(value='Destination Package', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='ondelete',
                                value=Constant(value='restrict', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="['|', '|', ('location_id', '=', False), ('location_id', '=', location_dest_id), ('id', '=', package_id)]", kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If set, the operations are packed into this package', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Datetime',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Date', kind=None)],
                        keywords=[
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
                            keyword(
                                arg='required',
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
                            Constant(value='From Owner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='check_company',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='When validating the transfer, the products will be taken from this owner.', kind=None),
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
                            Constant(value='From', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('usage', '!=', 'view')]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
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
                    targets=[Name(id='location_dest_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.location', kind=None),
                            Constant(value='To', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='domain',
                                value=Constant(value="[('usage', '!=', 'view')]", kind=None),
                            ),
                            keyword(
                                arg='check_company',
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
                    targets=[Name(id='lots_visible', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_lots_visible', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_partner_id', ctx=Store())],
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
                                value=Constant(value='picking_id.partner_id', kind=None),
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
                    targets=[Name(id='picking_code', ctx=Store())],
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
                                value=Constant(value='picking_id.picking_type_id.code', kind=None),
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
                    targets=[Name(id='picking_type_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.picking.type', kind=None),
                            Constant(value='Operation type', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_picking_type_id', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_picking_type_id', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='picking_type_use_create_lots', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='picking_id.picking_type_id.use_create_lots', kind=None),
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
                    targets=[Name(id='picking_type_use_existing_lots', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='picking_id.picking_type_id.use_existing_lots', kind=None),
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
                    targets=[Name(id='picking_type_entire_packs', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='picking_id.picking_type_id.show_entire_packs', kind=None),
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
                    targets=[Name(id='state', ctx=Store())],
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
                                value=Constant(value='move_id.state', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related_sudo',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_initial_demand_editable', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='move_id.is_initial_demand_editable', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_inventory', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='move_id.is_inventory', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='is_locked', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='move_id.is_locked', kind=None),
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
                    targets=[Name(id='consume_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move.line', kind=None),
                            Constant(value='stock_move_line_consume_rel', kind=None),
                            Constant(value='consume_line_id', kind=None),
                            Constant(value='produce_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Technical link to see who consumed what. ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='produce_line_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='stock.move.line', kind=None),
                            Constant(value='stock_move_line_consume_rel', kind=None),
                            Constant(value='produce_line_id', kind=None),
                            Constant(value='consume_line_id', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Technical link to see which line was produced with this. ', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='reference', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='move_id.reference', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='related_sudo',
                                value=Constant(value=False, kind=None),
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
                    targets=[Name(id='origin', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='move_id.origin', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Source', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='description_picking', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Description picking', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_lots_visible',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='picking', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='picking_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='picking', ctx=Load()),
                                                attr='picking_type_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='none', kind=None)],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='lots_visible',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='picking', ctx=Load()),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='use_existing_lots',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='picking', ctx=Load()),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='use_create_lots',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='lots_visible',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='none', kind=None)],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
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
                                Constant(value='picking_id.picking_type_id', kind=None),
                                Constant(value='product_id.tracking', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_picking_type_id',
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
                                    attr='picking_type_id',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Attribute(
                                        value=Name(id='line', ctx=Load()),
                                        attr='picking_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='picking_type_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='picking_id',
                                                    ctx=Load(),
                                                ),
                                                attr='picking_type_id',
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[Constant(value='picking_id', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_search_picking_type_id',
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
                        Return(
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='picking_id.picking_type_id', kind=None),
                                            Name(id='operator', ctx=Load()),
                                            Name(id='value', ctx=Load()),
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
                    name='_compute_product_qty',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='line', ctx=Load()),
                                            attr='product_qty',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='uom_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='HALF-UP', kind=None),
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='product_id', kind=None),
                                Constant(value='product_uom_id', kind=None),
                                Constant(value='product_uom_qty', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_set_product_qty',
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
                            value=Constant(value=' The meaning of product_qty field changed lately and is now a functional field computing the quantity\n        in the default product UoM. This code has been added to raise an error if a write is made given a value\n        for `product_qty`, where the same write should set the `product_uom_qty` field instead, in order to\n        detect errors. ', kind=None),
                        ),
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The requested operation cannot be processed because of a programming error setting the `product_qty` field instead of the `product_uom_qty`.', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            cause=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_lot_product',
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
                            target=Name(id='line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='line', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='line', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='sudo',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='This lot %(lot_name)s is incompatible with this product %(product_name)s', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_name',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='lot_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='name',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='product_name',
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='line', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='display_name',
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
                            args=[
                                Constant(value='lot_id', kind=None),
                                Constant(value='product_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_reserved_done_quantity',
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
                            target=Name(id='move_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='move_line', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='done', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='product_uom_qty',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_digits',
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Subscript(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='decimal.precision', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='precision_get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='A done move line should never have a reserved quantity.', kind=None)],
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
                            args=[Constant(value='product_uom_qty', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_positive_qty_done',
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
                                                value=Name(id='ml', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                            ops=[Lt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='ml', ctx=Store()),
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
                                                args=[Constant(value='You can not enter negative quantities.', kind=None)],
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
                            args=[Constant(value='qty_done', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_result_package_id',
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
                                attr='result_package_id',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_dest_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_putaway_strategy',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='package',
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='result_package_id',
                                                            ctx=Load(),
                                                        ),
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
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[Constant(value='result_package_id', kind=None)],
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
                                attr='product_id',
                                ctx=Load(),
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='result_package_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_done', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
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
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_dest_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_putaway_strategy',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_done', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='picking_id',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='product', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
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
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='picking_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
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
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='description_picking',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='_get_description',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='picking_type_id',
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
                                    targets=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='lots_visible',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='tracking',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='none', kind=None)],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='product_uom_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='category_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='category_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_uom',
                                                            ctx=Load(),
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
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
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
                                Constant(value='product_uom_id', kind=None),
                            ],
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
                        Expr(
                            value=Constant(value=' When the user is encoding a move line for a tracked product, we apply some logic to\n        help him. This includes:\n            - automatically switch `qty_done` to 1.0\n            - warn if he has already encoded `lot_name` in another move line\n            - warn (and update if appropriate) if the SN is in a different source location than selected\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
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
                                ops=[Eq()],
                                comparators=[Constant(value='serial', kind=None)],
                            ),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='qty_done',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='qty_done',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=1, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Constant(value=None, kind=None),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='move_lines_to_check', ctx=Store())],
                                            value=BinOp(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_get_similar_move_lines',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Sub(),
                                                right=Name(id='self', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_name',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='counter', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='Counter', ctx=Load()),
                                                        args=[
                                                            ListComp(
                                                                elt=Attribute(
                                                                    value=Name(id='line', ctx=Load()),
                                                                    attr='lot_name',
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='line', ctx=Store()),
                                                                        iter=Name(id='move_lines_to_check', ctx=Load()),
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
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Name(id='counter', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='lot_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Compare(
                                                                left=Subscript(
                                                                    value=Name(id='counter', ctx=Load()),
                                                                    slice=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='lot_name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Gt()],
                                                                comparators=[Constant(value=1, kind=None)],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='message', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='You cannot use the same serial number twice. Please correct the serial numbers encoded.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='lots', ctx=Store())],
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
                                                                                            Constant(value='name', kind=None),
                                                                                            Constant(value='=', kind=None),
                                                                                            Attribute(
                                                                                                value=Name(id='self', ctx=Load()),
                                                                                                attr='lot_name',
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
                                                                                ],
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='quants', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='lots', ctx=Load()),
                                                                                attr='quant_ids',
                                                                                ctx=Load(),
                                                                            ),
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
                                                                                        Compare(
                                                                                            left=Attribute(
                                                                                                value=Name(id='q', ctx=Load()),
                                                                                                attr='quantity',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            ops=[NotEq()],
                                                                                            comparators=[Constant(value=0, kind=None)],
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
                                                                                                        Constant(value='customer', kind=None),
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
                                                                If(
                                                                    test=Name(id='quants', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='message', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='_', ctx=Load()),
                                                                                args=[
                                                                                    Constant(value='Serial number (%s) already exists in location(s): %s. Please correct the serial number encoded.', kind=None),
                                                                                    Attribute(
                                                                                        value=Name(id='self', ctx=Load()),
                                                                                        attr='lot_name',
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
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='quants', ctx=Load()),
                                                                                                        attr='location_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
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
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='lot_id',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='counter', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='Counter', ctx=Load()),
                                                                args=[
                                                                    ListComp(
                                                                        elt=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='line', ctx=Load()),
                                                                                attr='lot_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='line', ctx=Store()),
                                                                                iter=Name(id='move_lines_to_check', ctx=Load()),
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
                                                        If(
                                                            test=BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='counter', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
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
                                                                        keywords=[],
                                                                    ),
                                                                    Compare(
                                                                        left=Subscript(
                                                                            value=Name(id='counter', ctx=Load()),
                                                                            slice=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='lot_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Gt()],
                                                                        comparators=[Constant(value=1, kind=None)],
                                                                    ),
                                                                ],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='message', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='You cannot use the same serial number twice. Please correct the serial numbers encoded.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Name(id='message', ctx=Store()),
                                                                                Name(id='recommended_location', ctx=Store()),
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
                                                                            Attribute(
                                                                                value=Name(id='self', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='picking_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='recommended_location', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='location_id',
                                                                                    ctx=Store(),
                                                                                ),
                                                                            ],
                                                                            value=Name(id='recommended_location', ctx=Load()),
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
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='message', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='res', ctx=Load()),
                                                    slice=Constant(value='warning', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
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
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='onchange',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='lot_name', kind=None),
                                Constant(value='lot_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_onchange_qty_done',
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
                            value=Constant(value=' When the user is encoding a move line for a tracked product, we apply some logic to\n        help him. This onchange will warn him if he set `qty_done` to a non-supported value.\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='qty_done',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='qty_done', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='product_uom_id',
                                                ctx=Load(),
                                            ),
                                            attr='_compute_quantity',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
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
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='user_has_groups',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='stock.group_stock_multi_locations', kind=None)],
                                                keywords=[],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='result_package_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='location_dest_id',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_putaway_strategy',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_done', ctx=Load()),
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
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_done', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
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
                                                        Name(id='qty_done', ctx=Load()),
                                                        Constant(value=1.0, kind=None),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
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
                                                ops=[NotEq()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='message', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='You can only process 1.0 %s of products with unique serial number.', kind=None),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='uom_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
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
                                                            value=Name(id='res', ctx=Load()),
                                                            slice=Constant(value='warning', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
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
                        Return(
                            value=Name(id='res', ctx=Load()),
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
                                Constant(value='qty_done', kind=None),
                                Constant(value='product_uom_id', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='init',
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
                                        value=Name(id='tools', ctx=Load()),
                                        attr='index_exists',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_cr',
                                            ctx=Load(),
                                        ),
                                        Constant(value='stock_move_line_free_reservation_index', kind=None),
                                    ],
                                    keywords=[],
                                ),
                            ),
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
                                        args=[Constant(value="\n                CREATE INDEX stock_move_line_free_reservation_index\n                ON\n                    stock_move_line (id, company_id, product_id, lot_id, location_id, owner_id, package_id)\n                WHERE\n                    (state IS NULL OR state NOT IN ('cancel', 'done')) AND product_qty > 0", kind=None)],
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
                        For(
                            target=Name(id='vals', ctx=Store()),
                            iter=Name(id='vals_list', ctx=Load()),
                            body=[
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_id', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='vals', ctx=Load()),
                                                    slice=Constant(value='company_id', kind=None),
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
                                                                slice=Constant(value='stock.move', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='browse',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='move_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    attr='company_id',
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
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='picking_id', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='company_id', kind=None),
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
                                                                        slice=Constant(value='stock.picking', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='browse',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='vals', ctx=Load()),
                                                                        slice=Constant(value='picking_id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            attr='company_id',
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mls', ctx=Store())],
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
                        FunctionDef(
                            name='create_move',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='move_line', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_move', ctx=Store())],
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
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='product_id', kind=None),
                                                    Constant(value='product_uom_qty', kind=None),
                                                    Constant(value='product_uom', kind=None),
                                                    Constant(value='description_picking', kind=None),
                                                    Constant(value='location_id', kind=None),
                                                    Constant(value='location_dest_id', kind=None),
                                                    Constant(value='picking_id', kind=None),
                                                    Constant(value='state', kind=None),
                                                    Constant(value='picking_type_id', kind=None),
                                                    Constant(value='restrict_partner_id', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='New Move:', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Add(),
                                                        right=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='display_name',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    IfExp(
                                                        test=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='move_line', ctx=Load()),
                                                                    attr='picking_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='move_line', ctx=Load()),
                                                                            attr='picking_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotEq()],
                                                                    comparators=[Constant(value='done', kind=None)],
                                                                ),
                                                            ],
                                                        ),
                                                        body=Constant(value=0, kind=None),
                                                        orelse=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='qty_done',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='product_uom_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='description_picking',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='location_dest_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='picking_type_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='owner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move_line', ctx=Load()),
                                                                attr='picking_id',
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
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='move_line', ctx=Load()),
                                            attr='move_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='new_move', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='move_line', ctx=Store()),
                            iter=Name(id='mls', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='move_line', ctx=Load()),
                                                    attr='picking_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='picking_id',
                                                ctx=Load(),
                                            ),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='moves', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='move_lines',
                                                        ctx=Load(),
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
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='x', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='move_line', ctx=Load()),
                                                                    attr='product_id',
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
                                            targets=[Name(id='moves', ctx=Store())],
                                            value=Call(
                                                func=Name(id='sorted', ctx=Load()),
                                                args=[Name(id='moves', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='key',
                                                        value=Lambda(
                                                            args=arguments(
                                                                posonlyargs=[],
                                                                args=[arg(arg='m', annotation=None, type_comment=None)],
                                                                vararg=None,
                                                                kwonlyargs=[],
                                                                kw_defaults=[],
                                                                kwarg=None,
                                                                defaults=[],
                                                            ),
                                                            body=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='m', ctx=Load()),
                                                                    attr='quantity_done',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Lt()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Name(id='m', ctx=Load()),
                                                                        attr='product_qty',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='reverse',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='moves', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='move_line', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Subscript(
                                                            value=Name(id='moves', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Expr(
                                                    value=Call(
                                                        func=Name(id='create_move', ctx=Load()),
                                                        args=[Name(id='move_line', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='create_move', ctx=Load()),
                                                args=[Name(id='move_line', ctx=Load())],
                                                keywords=[],
                                            ),
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
                                    Name(id='ml', ctx=Store()),
                                    Name(id='vals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='zip', ctx=Load()),
                                args=[
                                    Name(id='mls', ctx=Load()),
                                    Name(id='vals_list', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='picking_id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='picking_id',
                                                    ctx=Load(),
                                                ),
                                                attr='immediate_transfer',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='done', kind=None)],
                                            ),
                                            Compare(
                                                left=Constant(value='qty_done', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_uom_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='quantity_done',
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
                                            value=Name(id='ml', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='done', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='qty_done', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_uom_qty',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='quantity_done',
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
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='product', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='Quant', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='stock.quant', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='quantity', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='qty_done',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='in_date', ctx=Store())],
                                                    value=Constant(value=None, kind=None),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='available_qty', ctx=Store()),
                                                                Name(id='in_date', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Quant', ctx=Load()),
                                                            attr='_update_available_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='quantity', ctx=Load()),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='package_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='owner_id',
                                                                    ctx=Load(),
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
                                                            Compare(
                                                                left=Name(id='available_qty', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='lot_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='untracked_qty', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_get_available_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Constant(value=False, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
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
                                                            test=Name(id='untracked_qty', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='taken_from_untracked_qty', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='min', ctx=Load()),
                                                                        args=[
                                                                            Name(id='untracked_qty', ctx=Load()),
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
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Quant', ctx=Load()),
                                                                            attr='_update_available_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='taken_from_untracked_qty', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lot_id',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                            keyword(
                                                                                arg='package_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='owner_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='owner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Quant', ctx=Load()),
                                                                            attr='_update_available_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Name(id='taken_from_untracked_qty', ctx=Load()),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lot_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='lot_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='package_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='owner_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='owner_id',
                                                                                    ctx=Load(),
                                                                                ),
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
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Quant', ctx=Load()),
                                                            attr='_update_available_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='location_dest_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='quantity', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='result_package_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='owner_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='in_date',
                                                                value=Name(id='in_date', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='next_moves', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='move_dest_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='move', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotIn()],
                                                            comparators=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='done', kind=None),
                                                                        Constant(value='cancel', kind=None),
                                                                    ],
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='next_moves', ctx=Load()),
                                                    attr='_do_unreserve',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='next_moves', ctx=Load()),
                                                    attr='_action_assign',
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='mls', ctx=Load()),
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
                            arg(arg='vals', annotation=None, type_comment=None),
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
                                args=[Constant(value='bypass_reservation_update', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Name(id='super', ctx=Load()),
                                                args=[
                                                    Name(id='StockMoveLine', ctx=Load()),
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Constant(value='product_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Call(
                                        func=Name(id='any', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Call(
                                                                func=Attribute(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value='state', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[Constant(value='draft', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='product_id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotEq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='ml', ctx=Store()),
                                                        iter=Name(id='self', ctx=Load()),
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
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value="Changing the product is only allowed in 'Draft' state.", kind=None)],
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
                            targets=[Name(id='moves_to_recompute_state', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.move', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='Quant', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.quant', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='precision', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='decimal.precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='precision_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='triggers', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='location_id', kind=None),
                                            Constant(value='stock.location', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='location_dest_id', kind=None),
                                            Constant(value='stock.location', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lot_id', kind=None),
                                            Constant(value='stock.production.lot', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='package_id', kind=None),
                                            Constant(value='stock.quant.package', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='result_package_id', kind=None),
                                            Constant(value='stock.quant.package', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='owner_id', kind=None),
                                            Constant(value='res.partner', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='product_uom_id', kind=None),
                                            Constant(value='uom.uom', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='updates', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='model', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='triggers', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='key', ctx=Load()),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='updates', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
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
                                                        slice=Name(id='model', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Name(id='vals', ctx=Load()),
                                                        slice=Name(id='key', ctx=Load()),
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
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='result_package_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='updates', ctx=Load())],
                            ),
                            body=[
                                For(
                                    target=Name(id='ml', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='package_level_id',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='result_package_id', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='package_level_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='package_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='updates', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='result_package_id', kind=None)],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='package_level', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='package_level_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='package_level_id',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=False, kind=None),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='package_level', ctx=Load()),
                                                            attr='unlink',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='updates', ctx=Load()),
                                    Compare(
                                        left=Constant(value='product_uom_qty', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                For(
                                    target=Name(id='ml', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[In()],
                                                            comparators=[
                                                                List(
                                                                    elts=[
                                                                        Constant(value='partially_available', kind=None),
                                                                        Constant(value='assigned', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='product', kind=None)],
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Constant(value='product_uom_qty', kind=None),
                                                ops=[In()],
                                                comparators=[Name(id='vals', ctx=Load())],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_product_uom_qty', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Subscript(
                                                                value=Name(id='vals', ctx=Load()),
                                                                slice=Constant(value='product_uom_qty', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
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
                                                                Name(id='new_product_uom_qty', ctx=Load()),
                                                                Constant(value=0, kind=None),
                                                            ],
                                                            keywords=[
                                                                keyword(
                                                                    arg='precision_rounding',
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
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
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    body=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Name(id='UserError', ctx=Load()),
                                                                args=[
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Reserving a negative quantity is not allowed.', kind=None)],
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
                                                Assign(
                                                    targets=[Name(id='new_product_uom_qty', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_should_bypass_reservation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_update_reserved_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='product_qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='lot_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
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
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='UserError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                If(
                                                                    test=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='lot_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='Quant', ctx=Load()),
                                                                                    attr='_update_reserved_quantity',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='location_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    UnaryOp(
                                                                                        op=USub(),
                                                                                        operand=Attribute(
                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                            attr='product_qty',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='lot_id',
                                                                                        value=Constant(value=False, kind=None),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='package_id',
                                                                                        value=Attribute(
                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                            attr='package_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='owner_id',
                                                                                        value=Attribute(
                                                                                            value=Name(id='ml', ctx=Load()),
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
                                                                        ),
                                                                    ],
                                                                    orelse=[Raise(exc=None, cause=None)],
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
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_should_bypass_reservation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='updates', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Constant(value='location_id', kind=None),
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
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
                                            body=[
                                                Assign(
                                                    targets=[Name(id='reserved_qty', ctx=Store())],
                                                    value=Constant(value=0, kind=None),
                                                    type_comment=None,
                                                ),
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='q', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_update_reserved_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Attribute(
                                                                            value=Name(id='updates', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='location_id', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    Name(id='new_product_uom_qty', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='updates', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Constant(value='lot_id', kind=None),
                                                                                Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='lot_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='updates', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Constant(value='package_id', kind=None),
                                                                                Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='updates', ctx=Load()),
                                                                                attr='get',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[
                                                                                Constant(value='owner_id', kind=None),
                                                                                Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='owner_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                            keywords=[],
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
                                                        Assign(
                                                            targets=[Name(id='reserved_qty', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='sum', ctx=Load()),
                                                                args=[
                                                                    ListComp(
                                                                        elt=Subscript(
                                                                            value=Name(id='x', ctx=Load()),
                                                                            slice=Constant(value=1, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        generators=[
                                                                            comprehension(
                                                                                target=Name(id='x', ctx=Store()),
                                                                                iter=Name(id='q', ctx=Load()),
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
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='UserError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                If(
                                                                    test=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='updates', ctx=Load()),
                                                                            attr='get',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='lot_id', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Try(
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='q', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='Quant', ctx=Load()),
                                                                                            attr='_update_reserved_quantity',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='ml', ctx=Load()),
                                                                                                attr='product_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='updates', ctx=Load()),
                                                                                                    attr='get',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Constant(value='location_id', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                                        attr='location_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            Name(id='new_product_uom_qty', ctx=Load()),
                                                                                        ],
                                                                                        keywords=[
                                                                                            keyword(
                                                                                                arg='lot_id',
                                                                                                value=Constant(value=False, kind=None),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='package_id',
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='updates', ctx=Load()),
                                                                                                        attr='get',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[
                                                                                                        Constant(value='package_id', kind=None),
                                                                                                        Attribute(
                                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                                            attr='package_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
                                                                                                ),
                                                                                            ),
                                                                                            keyword(
                                                                                                arg='owner_id',
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='updates', ctx=Load()),
                                                                                                        attr='get',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[
                                                                                                        Constant(value='owner_id', kind=None),
                                                                                                        Attribute(
                                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                                            attr='owner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
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
                                                                                Assign(
                                                                                    targets=[Name(id='reserved_qty', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Name(id='sum', ctx=Load()),
                                                                                        args=[
                                                                                            ListComp(
                                                                                                elt=Subscript(
                                                                                                    value=Name(id='x', ctx=Load()),
                                                                                                    slice=Constant(value=1, kind=None),
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                generators=[
                                                                                                    comprehension(
                                                                                                        target=Name(id='x', ctx=Store()),
                                                                                                        iter=Name(id='q', ctx=Load()),
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
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='reserved_qty', ctx=Load()),
                                                        ops=[NotEq()],
                                                        comparators=[Name(id='new_product_uom_qty', ctx=Load())],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='new_product_uom_qty', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='product_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='_compute_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='reserved_qty', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_uom_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='rounding_method',
                                                                        value=Constant(value='HALF-UP', kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        AugAssign(
                                                            target=Name(id='moves_to_recompute_state', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='with_context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='bypass_reservation_update',
                                                                                value=Constant(value=True, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    attr='product_uom_qty',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Name(id='new_product_uom_qty', ctx=Load()),
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
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='updates', ctx=Load()),
                                    Compare(
                                        left=Constant(value='qty_done', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='next_moves', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='mls', ctx=Store())],
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
                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='done', kind=None)],
                                                        ),
                                                        Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='type',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='product', kind=None)],
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
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='updates', ctx=Load()),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='mls', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='mls', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=UnaryOp(
                                                            op=Not(),
                                                            operand=Call(
                                                                func=Name(id='float_is_zero', ctx=Load()),
                                                                args=[
                                                                    BinOp(
                                                                        left=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='qty_done',
                                                                            ctx=Load(),
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Subscript(
                                                                            value=Name(id='vals', ctx=Load()),
                                                                            slice=Constant(value='qty_done', kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='precision_rounding',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='product_uom_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='rounding',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
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
                                For(
                                    target=Name(id='ml', ctx=Store()),
                                    iter=Name(id='mls', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_done_orig', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='rounding_method',
                                                        value=Constant(value='HALF-UP', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='in_date', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='Quant', ctx=Load()),
                                                        attr='_update_available_quantity',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='location_dest_id',
                                                            ctx=Load(),
                                                        ),
                                                        UnaryOp(
                                                            op=USub(),
                                                            operand=Name(id='qty_done_orig', ctx=Load()),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='lot_id',
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='lot_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='package_id',
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='result_package_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        keyword(
                                                            arg='owner_id',
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='owner_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Quant', ctx=Load()),
                                                    attr='_update_available_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_done_orig', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lot_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='lot_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='package_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='package_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='owner_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='owner_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='in_date',
                                                        value=Name(id='in_date', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='product_id', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='location_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='location_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='location_dest_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='location_dest_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='qty_done', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='qty_done', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='qty_done',
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
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='lot_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='lot_id',
                                                        ctx=Load(),
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
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='package_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='package_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='result_package_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='result_package_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='result_package_id',
                                                        ctx=Load(),
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
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='owner_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='owner_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='product_uom_id', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='updates', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='product_uom_id', kind=None),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='quantity', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='product_uom_id', ctx=Load()),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='qty_done', ctx=Load()),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='rounding_method',
                                                        value=Constant(value='HALF-UP', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_should_bypass_reservation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='location_id', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='_free_reservation',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='product_id', ctx=Load()),
                                                            Name(id='location_id', ctx=Load()),
                                                            Name(id='quantity', ctx=Load()),
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
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[Name(id='quantity', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_digits',
                                                            value=Name(id='precision', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='available_qty', ctx=Store()),
                                                                Name(id='in_date', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Quant', ctx=Load()),
                                                            attr='_update_available_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='product_id', ctx=Load()),
                                                            Name(id='location_id', ctx=Load()),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Name(id='quantity', ctx=Load()),
                                                            ),
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
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Name(id='available_qty', ctx=Load()),
                                                                ops=[Lt()],
                                                                comparators=[Constant(value=0, kind=None)],
                                                            ),
                                                            Name(id='lot_id', ctx=Load()),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='untracked_qty', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
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
                                                                        value=Constant(value=False, kind=None),
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
                                                            test=Name(id='untracked_qty', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='taken_from_untracked_qty', ctx=Store())],
                                                                    value=Call(
                                                                        func=Name(id='min', ctx=Load()),
                                                                        args=[
                                                                            Name(id='untracked_qty', ctx=Load()),
                                                                            Call(
                                                                                func=Name(id='abs', ctx=Load()),
                                                                                args=[Name(id='available_qty', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Quant', ctx=Load()),
                                                                            attr='_update_available_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='product_id', ctx=Load()),
                                                                            Name(id='location_id', ctx=Load()),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Name(id='taken_from_untracked_qty', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lot_id',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                            keyword(
                                                                                arg='package_id',
                                                                                value=Name(id='package_id', ctx=Load()),
                                                                            ),
                                                                            keyword(
                                                                                arg='owner_id',
                                                                                value=Name(id='owner_id', ctx=Load()),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Quant', ctx=Load()),
                                                                            attr='_update_available_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Name(id='product_id', ctx=Load()),
                                                                            Name(id='location_id', ctx=Load()),
                                                                            Name(id='taken_from_untracked_qty', ctx=Load()),
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
                                                                        ],
                                                                    ),
                                                                ),
                                                                If(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Call(
                                                                            func=Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='move_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='_should_bypass_reservation',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[Name(id='location_id', ctx=Load())],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    body=[
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='_free_reservation',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='product_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='location_id', ctx=Load()),
                                                                                    Name(id='untracked_qty', ctx=Load()),
                                                                                ],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='lot_id',
                                                                                        value=Constant(value=False, kind=None),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='package_id',
                                                                                        value=Name(id='package_id', ctx=Load()),
                                                                                    ),
                                                                                    keyword(
                                                                                        arg='owner_id',
                                                                                        value=Name(id='owner_id', ctx=Load()),
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
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Quant', ctx=Load()),
                                                            attr='_update_available_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='product_id', ctx=Load()),
                                                            Name(id='location_dest_id', ctx=Load()),
                                                            Name(id='quantity', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Name(id='lot_id', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Name(id='result_package_id', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Name(id='owner_id', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='in_date',
                                                                value=Name(id='in_date', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                        AugAssign(
                                            target=Name(id='next_moves', ctx=Store()),
                                            op=BitOr(),
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='move_dest_ids',
                                                        ctx=Load(),
                                                    ),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='move', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[NotIn()],
                                                            comparators=[
                                                                Tuple(
                                                                    elts=[
                                                                        Constant(value='done', kind=None),
                                                                        Constant(value='cancel', kind=None),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='picking_id',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='_log_message',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='ml', ctx=Load()),
                                                            Constant(value='stock.track_move_template', kind=None),
                                                            Name(id='vals', ctx=Load()),
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
                                            Name(id='StockMoveLine', ctx=Load()),
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
                            test=Compare(
                                left=Constant(value='qty_done', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_id', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='scrapped',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='move', ctx=Load()),
                                                                attr='scrap_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='write',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Dict(
                                                                keys=[Constant(value='scrap_qty', kind=None)],
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='move', ctx=Load()),
                                                                        attr='quantity_done',
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
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='updates', ctx=Load()),
                                    Compare(
                                        left=Constant(value='qty_done', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='moves', ctx=Store())],
                                    value=Call(
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
                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='done', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='mapped',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='move_id', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='moves', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
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
                                                            args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=BoolOp(
                                                            op=And(),
                                                            values=[
                                                                Compare(
                                                                    left=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='state',
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[NotIn()],
                                                                    comparators=[
                                                                        Tuple(
                                                                            elts=[
                                                                                Constant(value='done', kind=None),
                                                                                Constant(value='cancel', kind=None),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='move_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='picking_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='immediate_transfer',
                                                                    ctx=Load(),
                                                                ),
                                                                UnaryOp(
                                                                    op=Not(),
                                                                    operand=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_uom_qty',
                                                                        ctx=Load(),
                                                                    ),
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
                                        args=[Constant(value='move_id', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                                For(
                                    target=Name(id='move', ctx=Store()),
                                    iter=Name(id='moves', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='quantity_done',
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
                                            value=Name(id='next_moves', ctx=Load()),
                                            attr='_do_unreserve',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='next_moves', ctx=Load()),
                                            attr='_action_assign',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='moves_to_recompute_state', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='moves_to_recompute_state', ctx=Load()),
                                            attr='_recompute_state',
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
                    name='_unlink_except_done_or_cancel',
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
                            target=Name(id='ml', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='ml', ctx=Load()),
                                            attr='state',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='done', kind=None),
                                                    Constant(value='cancel', kind=None),
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
                                                        args=[Constant(value='You can not delete product moves if the picking is done. You can only correct the done quantities.', kind=None)],
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
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='ondelete',
                                ctx=Load(),
                            ),
                            args=[],
                            keywords=[
                                keyword(
                                    arg='at_uninstall',
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='unlink',
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
                            targets=[Name(id='precision', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='decimal.precision', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='precision_get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='Product Unit of Measure', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ml', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='type',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='product', kind=None)],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='_should_bypass_reservation',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='location_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_digits',
                                                            value=Name(id='precision', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Try(
                                            body=[
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
                                                            attr='_update_reserved_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            UnaryOp(
                                                                op=USub(),
                                                                operand=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_qty',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='package_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
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
                                                ),
                                            ],
                                            handlers=[
                                                ExceptHandler(
                                                    type=Name(id='UserError', ctx=Load()),
                                                    name=None,
                                                    body=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='lot_id',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
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
                                                                            attr='_update_reserved_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='product_qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lot_id',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                            keyword(
                                                                                arg='package_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='owner_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
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
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=UnaryOp(
                                                                        op=Not(),
                                                                        operand=Call(
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
                                                                                Name(id='MODULE_UNINSTALL_FLAG', ctx=Load()),
                                                                                Constant(value=False, kind=None),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                    ),
                                                                    body=[Raise(exc=None, cause=None)],
                                                                    orelse=[],
                                                                ),
                                                            ],
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
                        Assign(
                            targets=[Name(id='moves', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='mapped',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='move_id', kind=None)],
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
                                            Name(id='StockMoveLine', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='moves', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='moves', ctx=Load()),
                                                    attr='with_prefetch',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='_recompute_state',
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
                    name='_action_done',
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
                            value=Constant(value=" This method is called during a move's `action_done`. It'll actually move a quant from\n        the source location to the destination location, and unreserve if needed in the source\n        location.\n\n        This method is intended to be called on all the move lines of a move. This method is not\n        intended to be called when editing a `done` move (that's what the override of `write` here\n        is done.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='Quant', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.quant', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ml_ids_tracked_without_lot', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedSet', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ml_ids_to_delete', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedSet', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ml_ids_to_create_lot', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedSet', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ml', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='uom_qty', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='HALF-UP', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='precision_digits', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='decimal.precision', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='precision_get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='Product Unit of Measure', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='qty_done', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_round', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_digits',
                                                value=Name(id='precision_digits', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='rounding_method',
                                                value=Constant(value='HALF-UP', kind=None),
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
                                                Name(id='uom_qty', ctx=Load()),
                                                Name(id='qty_done', ctx=Load()),
                                            ],
                                            keywords=[
                                                keyword(
                                                    arg='precision_digits',
                                                    value=Name(id='precision_digits', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='The quantity done for the product "%s" doesn\'t respect the rounding precision                                   defined on the unit of measure "%s". Please change the quantity done or the                                   rounding precision of your unit of measure.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_uom_id',
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
                                Assign(
                                    targets=[Name(id='qty_done_float_compared', ctx=Store())],
                                    value=Call(
                                        func=Name(id='float_compare', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                            Constant(value=0, kind=None),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='precision_rounding',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='rounding',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='qty_done_float_compared', ctx=Load()),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='none', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='picking_type_id', ctx=Store())],
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='move_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='picking_type_id',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='picking_type_id', ctx=Load()),
                                                    body=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='picking_type_id', ctx=Load()),
                                                                attr='use_create_lots',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='lot_name',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='lot_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='lot', ctx=Store())],
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
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                                            attr='company_id',
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
                                                                                                    Constant(value='product_id', kind=None),
                                                                                                    Constant(value='=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='ml', ctx=Load()),
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
                                                                                                    Constant(value='name', kind=None),
                                                                                                    Constant(value='=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                                        attr='lot_name',
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
                                                                            test=Name(id='lot', ctx=Load()),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[
                                                                                        Attribute(
                                                                                            value=Name(id='ml', ctx=Load()),
                                                                                            attr='lot_id',
                                                                                            ctx=Store(),
                                                                                        ),
                                                                                    ],
                                                                                    value=Attribute(
                                                                                        value=Name(id='lot', ctx=Load()),
                                                                                        attr='id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='ml_ids_to_create_lot', ctx=Load()),
                                                                                            attr='add',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Attribute(
                                                                                                value=Name(id='ml', ctx=Load()),
                                                                                                attr='id',
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
                                                                ),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=BoolOp(
                                                                        op=And(),
                                                                        values=[
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='picking_type_id', ctx=Load()),
                                                                                    attr='use_create_lots',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=Not(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='picking_type_id', ctx=Load()),
                                                                                    attr='use_existing_lots',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    body=[Continue()],
                                                                    orelse=[],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='is_inventory',
                                                                ctx=Load(),
                                                            ),
                                                            body=[Continue()],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[NotIn()],
                                                                comparators=[Name(id='ml_ids_to_create_lot', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ml_ids_tracked_without_lot', ctx=Load()),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
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
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='qty_done_float_compared', ctx=Load()),
                                                ops=[Lt()],
                                                comparators=[Constant(value=0, kind=None)],
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='UserError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='No negative quantities allowed', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='is_inventory',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ml_ids_to_delete', ctx=Load()),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
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
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='ml_ids_tracked_without_lot', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='mls_tracked_without_lot', ctx=Store())],
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
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ml_ids_tracked_without_lot', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            BinOp(
                                                left=Call(
                                                    func=Name(id='_', ctx=Load()),
                                                    args=[Constant(value='You need to supply a Lot/Serial Number for product: \n - ', kind=None)],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Constant(value='\n - ', kind=None),
                                                        attr='join',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='mls_tracked_without_lot', ctx=Load()),
                                                                attr='mapped',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='product_id.display_name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    keywords=[],
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
                        Assign(
                            targets=[Name(id='ml_to_create_lot', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ml_ids_to_create_lot', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ml_to_create_lot', ctx=Load()),
                                    attr='_create_and_assign_production_lot',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mls_to_delete', ctx=Store())],
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
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='ml_ids_to_delete', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mls_to_delete', ctx=Load()),
                                    attr='unlink',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mls_todo', ctx=Store())],
                            value=BinOp(
                                left=Name(id='self', ctx=Load()),
                                op=Sub(),
                                right=Name(id='mls_to_delete', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='mls_todo', ctx=Load()),
                                    attr='_check_company',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ml_ids_to_ignore', ctx=Store())],
                            value=Call(
                                func=Name(id='OrderedSet', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ml', ctx=Store()),
                            iter=Name(id='mls_todo', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='product_id',
                                                ctx=Load(),
                                            ),
                                            attr='type',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='product', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='rounding', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
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
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_should_bypass_reservation',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='location_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Call(
                                                            func=Name(id='float_compare', ctx=Load()),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='qty_done',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_uom_qty',
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
                                                        ops=[Gt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='qty_done_product_uom', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='qty_done',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='extra_qty', ctx=Store())],
                                                    value=BinOp(
                                                        left=Name(id='qty_done_product_uom', ctx=Load()),
                                                        op=Sub(),
                                                        right=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='_free_reservation',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='extra_qty', ctx=Load()),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='package_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='owner_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='ml_ids_to_ignore',
                                                                value=Name(id='ml_ids_to_ignore', ctx=Load()),
                                                            ),
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
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='move_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='_should_bypass_reservation',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='location_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Compare(
                                                        left=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='type',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='product', kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_update_reserved_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='product_qty',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='lot_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
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
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='UserError', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='Quant', ctx=Load()),
                                                                            attr='_update_reserved_quantity',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='product_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='ml', ctx=Load()),
                                                                                attr='location_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            UnaryOp(
                                                                                op=USub(),
                                                                                operand=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='product_qty',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='lot_id',
                                                                                value=Constant(value=False, kind=None),
                                                                            ),
                                                                            keyword(
                                                                                arg='package_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
                                                                                    attr='package_id',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                            keyword(
                                                                                arg='owner_id',
                                                                                value=Attribute(
                                                                                    value=Name(id='ml', ctx=Load()),
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
                                            targets=[Name(id='quantity', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_compute_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='rounding_method',
                                                        value=Constant(value='HALF-UP', kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Tuple(
                                                    elts=[
                                                        Name(id='available_qty', ctx=Store()),
                                                        Name(id='in_date', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Quant', ctx=Load()),
                                                    attr='_update_available_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='location_id',
                                                        ctx=Load(),
                                                    ),
                                                    UnaryOp(
                                                        op=USub(),
                                                        operand=Name(id='quantity', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lot_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='lot_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='package_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='package_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='owner_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='owner_id',
                                                            ctx=Load(),
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
                                                    Compare(
                                                        left=Name(id='available_qty', ctx=Load()),
                                                        ops=[Lt()],
                                                        comparators=[Constant(value=0, kind=None)],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='lot_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='untracked_qty', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='Quant', ctx=Load()),
                                                            attr='_get_available_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='location_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='lot_id',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                            keyword(
                                                                arg='package_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='package_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='owner_id',
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
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
                                                    test=Name(id='untracked_qty', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='taken_from_untracked_qty', ctx=Store())],
                                                            value=Call(
                                                                func=Name(id='min', ctx=Load()),
                                                                args=[
                                                                    Name(id='untracked_qty', ctx=Load()),
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
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_update_available_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    UnaryOp(
                                                                        op=USub(),
                                                                        operand=Name(id='taken_from_untracked_qty', ctx=Load()),
                                                                    ),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Constant(value=False, kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='owner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='Quant', ctx=Load()),
                                                                    attr='_update_available_quantity',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='product_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='ml', ctx=Load()),
                                                                        attr='location_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='taken_from_untracked_qty', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='lot_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='lot_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='package_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='package_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='owner_id',
                                                                        value=Attribute(
                                                                            value=Name(id='ml', ctx=Load()),
                                                                            attr='owner_id',
                                                                            ctx=Load(),
                                                                        ),
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
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Quant', ctx=Load()),
                                                    attr='_update_available_quantity',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='ml', ctx=Load()),
                                                        attr='location_dest_id',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='quantity', ctx=Load()),
                                                ],
                                                keywords=[
                                                    keyword(
                                                        arg='lot_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='lot_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='package_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='result_package_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='owner_id',
                                                        value=Attribute(
                                                            value=Name(id='ml', ctx=Load()),
                                                            attr='owner_id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='in_date',
                                                        value=Name(id='in_date', ctx=Load()),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='ml_ids_to_ignore', ctx=Load()),
                                            attr='add',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
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
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mls_todo', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='bypass_reservation_update',
                                                value=Constant(value=True, kind=None),
                                            ),
                                        ],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_uom_qty', kind=None),
                                            Constant(value='date', kind=None),
                                        ],
                                        values=[
                                            Constant(value=0.0, kind=None),
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
                    name='_get_similar_move_lines',
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
                            targets=[Name(id='lines', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.move.line', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='picking_id', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='move_id',
                                    ctx=Load(),
                                ),
                                body=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='move_id',
                                        ctx=Load(),
                                    ),
                                    attr='picking_id',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='picking_id',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='picking_id', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='lines', ctx=Store()),
                                    op=BitOr(),
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='picking_id', ctx=Load()),
                                                attr='move_line_ids',
                                                ctx=Load(),
                                            ),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Compare(
                                                            left=Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='product_id',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_id',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='lot_name',
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
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_create_and_assign_production_lot',
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
                            value=Constant(value=' Creates and assign new production lots for move lines.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lot_vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key_to_index', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='key_to_mls', ctx=Store())],
                            value=Call(
                                func=Name(id='defaultdict', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),
                                        body=Subscript(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='env',
                                                ctx=Load(),
                                            ),
                                            slice=Constant(value='stock.move.line', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ml', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='key', ctx=Store())],
                                    value=Tuple(
                                        elts=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='company_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='product_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='ml', ctx=Load()),
                                                attr='lot_name',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Subscript(
                                        value=Name(id='key_to_mls', ctx=Load()),
                                        slice=Name(id='key', ctx=Load()),
                                        ctx=Store(),
                                    ),
                                    op=BitOr(),
                                    value=Name(id='ml', ctx=Load()),
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='ml', ctx=Load()),
                                                    attr='tracking',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='lot', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='key', ctx=Load()),
                                                ops=[NotIn()],
                                                comparators=[Name(id='key_to_index', ctx=Load())],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='key_to_index', ctx=Load()),
                                                    slice=Name(id='key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='len', ctx=Load()),
                                                args=[Name(id='lot_vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='lot_vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='company_id', kind=None),
                                                            Constant(value='name', kind=None),
                                                            Constant(value='product_id', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='company_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='ml', ctx=Load()),
                                                                attr='lot_name',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='ml', ctx=Load()),
                                                                    attr='product_id',
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
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='lots', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='lot_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='key', ctx=Store()),
                                    Name(id='mls', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='key_to_mls', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='mls', ctx=Load()),
                                            attr='_assign_production_lot',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Name(id='lots', ctx=Load()),
                                                        slice=Subscript(
                                                            value=Name(id='key_to_index', ctx=Load()),
                                                            slice=Name(id='key', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_prefetch',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='lots', ctx=Load()),
                                                        attr='_ids',
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
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_assign_production_lot',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='lot', annotation=None, type_comment=None),
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
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='lot_id', kind=None)],
                                        values=[
                                            Attribute(
                                                value=Name(id='lot', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
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
                    name='_reservation_is_updatable',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='quantity', annotation=None, type_comment=None),
                            arg(arg='reserved_quant', annotation=None, type_comment=None),
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
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
                                        ops=[NotEq()],
                                        comparators=[Constant(value='serial', kind=None)],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='location_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='reserved_quant', ctx=Load()),
                                                    attr='location_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='lot_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='reserved_quant', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='package_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='reserved_quant', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    Compare(
                                        left=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='owner_id',
                                                ctx=Load(),
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='reserved_quant', ctx=Load()),
                                                    attr='owner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_log_message',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='record', annotation=None, type_comment=None),
                            arg(arg='move', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='vals', ctx=Load()),
                                    attr='copy',
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
                                    Compare(
                                        left=Constant(value='lot_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='lot_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='lot_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='lot_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='location_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='location_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='location_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='location_dest_id', kind=None),
                                ops=[In()],
                                comparators=[Name(id='vals', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='location_dest_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='vals', ctx=Load()),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='location_dest_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='name',
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
                                    Compare(
                                        left=Constant(value='package_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='package_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='package_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='package_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                        attr='name',
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
                                    Compare(
                                        left=Constant(value='package_result_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='package_result_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='package_result_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='result_package_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                                    args=[Constant(value='result_package_id', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='name',
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
                                    Compare(
                                        left=Constant(value='owner_id', kind=None),
                                        ops=[In()],
                                        comparators=[Name(id='vals', ctx=Load())],
                                    ),
                                    Compare(
                                        left=Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='owner_id', kind=None),
                                            ctx=Load(),
                                        ),
                                        ops=[NotEq()],
                                        comparators=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='move', ctx=Load()),
                                                    attr='owner_id',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
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
                                            value=Name(id='data', ctx=Load()),
                                            slice=Constant(value='owner_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
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
                                        attr='name',
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
                                    value=Name(id='record', ctx=Load()),
                                    attr='message_post_with_view',
                                    ctx=Load(),
                                ),
                                args=[Name(id='template', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='values',
                                        value=Dict(
                                            keys=[
                                                Constant(value='move', kind=None),
                                                Constant(value='vals', kind=None),
                                            ],
                                            values=[
                                                Name(id='move', ctx=Load()),
                                                Call(
                                                    func=Name(id='dict', ctx=Load()),
                                                    args=[Name(id='vals', ctx=Load())],
                                                    keywords=[
                                                        keyword(
                                                            arg=None,
                                                            value=Name(id='data', ctx=Load()),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='subtype_id',
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
                                                args=[Constant(value='mail.mt_note', kind=None)],
                                                keywords=[],
                                            ),
                                            attr='id',
                                            ctx=Load(),
                                        ),
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
                    name='_free_reservation',
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
                            arg(arg='ml_ids_to_ignore', annotation=None, type_comment=None),
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
                            value=Constant(value=' When editing a done move line or validating one with some forced quantities, it is\n        possible to impact quants that were not reserved. It is therefore necessary to edit or\n        unlink the move lines that reserved a quantity now unavailable.\n\n        :param ml_ids_to_ignore: OrderedSet of `stock.move.line` ids that should NOT be unreserved\n        ', kind=None),
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
                            test=Compare(
                                left=Name(id='ml_ids_to_ignore', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ml_ids_to_ignore', ctx=Store())],
                                    value=Call(
                                        func=Name(id='OrderedSet', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        AugAssign(
                            target=Name(id='ml_ids_to_ignore', ctx=Store()),
                            op=BitOr(),
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='available_quantity', ctx=Store())],
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
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='quantity', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Name(id='available_quantity', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='outdated_move_lines_domain', ctx=Store())],
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='state', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    List(
                                                        elts=[
                                                            Constant(value='done', kind=None),
                                                            Constant(value='cancel', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                                    IfExp(
                                                        test=Name(id='lot_id', ctx=Load()),
                                                        body=Attribute(
                                                            value=Name(id='lot_id', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                            Tuple(
                                                elts=[
                                                    Constant(value='owner_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    IfExp(
                                                        test=Name(id='owner_id', ctx=Load()),
                                                        body=Attribute(
                                                            value=Name(id='owner_id', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='package_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    IfExp(
                                                        test=Name(id='package_id', ctx=Load()),
                                                        body=Attribute(
                                                            value=Name(id='package_id', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Constant(value=False, kind=None),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='product_qty', kind=None),
                                                    Constant(value='>', kind=None),
                                                    Constant(value=0.0, kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[Name(id='ml_ids_to_ignore', ctx=Load())],
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
                                Assign(
                                    targets=[Name(id='current_picking_first', ctx=Store())],
                                    value=Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='cand', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Tuple(
                                            elts=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='cand', ctx=Load()),
                                                        attr='picking_id',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[NotEq()],
                                                    comparators=[
                                                        Attribute(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='picking_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                                IfExp(
                                                    test=BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='cand', ctx=Load()),
                                                                attr='picking_id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='cand', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=UnaryOp(
                                                        op=USub(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=BoolOp(
                                                                    op=Or(),
                                                                    values=[
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='cand', ctx=Load()),
                                                                                attr='picking_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='scheduled_date',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='cand', ctx=Load()),
                                                                                attr='move_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='date',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                ),
                                                                attr='timestamp',
                                                                ctx=Load(),
                                                            ),
                                                            args=[],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    orelse=UnaryOp(
                                                        op=USub(),
                                                        operand=Attribute(
                                                            value=Name(id='cand', ctx=Load()),
                                                            attr='id',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='outdated_candidates', ctx=Store())],
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
                                                args=[Name(id='outdated_move_lines_domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='sorted',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='current_picking_first', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='move_to_recompute_state', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='stock.move', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='to_unlink_candidate_ids', ctx=Store())],
                                    value=Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='rounding', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='product_uom_id',
                                            ctx=Load(),
                                        ),
                                        attr='rounding',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='candidate', ctx=Store()),
                                    iter=Name(id='outdated_candidates', ctx=Load()),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Call(
                                                    func=Name(id='float_compare', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='candidate', ctx=Load()),
                                                            attr='product_qty',
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='quantity', ctx=Load()),
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
                                            body=[
                                                AugAssign(
                                                    target=Name(id='quantity', ctx=Store()),
                                                    op=Sub(),
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='product_qty',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                If(
                                                    test=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='move_to_recompute_state', ctx=Store()),
                                                            op=BitOr(),
                                                            value=Attribute(
                                                                value=Name(id='candidate', ctx=Load()),
                                                                attr='move_id',
                                                                ctx=Load(),
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[
                                                                Attribute(
                                                                    value=Name(id='candidate', ctx=Load()),
                                                                    attr='product_uom_qty',
                                                                    ctx=Store(),
                                                                ),
                                                            ],
                                                            value=Constant(value=0.0, kind=None),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='to_unlink_candidate_ids', ctx=Load()),
                                                                    attr='add',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='candidate', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Name(id='float_is_zero', ctx=Load()),
                                                        args=[Name(id='quantity', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='precision_rounding',
                                                                value=Name(id='rounding', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[Break()],
                                                    orelse=[],
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[Name(id='quantity_split', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='float_round', ctx=Load()),
                                                        args=[
                                                            BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='candidate', ctx=Load()),
                                                                    attr='product_qty',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Sub(),
                                                                right=Name(id='quantity', ctx=Load()),
                                                            ),
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
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='candidate', ctx=Load()),
                                                            attr='product_uom_qty',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='product_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='uom_id',
                                                                ctx=Load(),
                                                            ),
                                                            attr='_compute_quantity',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='quantity_split', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='candidate', ctx=Load()),
                                                                attr='product_uom_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[
                                                            keyword(
                                                                arg='rounding_method',
                                                                value=Constant(value='HALF-UP', kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='move_to_recompute_state', ctx=Store()),
                                                    op=BitOr(),
                                                    value=Attribute(
                                                        value=Name(id='candidate', ctx=Load()),
                                                        attr='move_id',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                Expr(
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
                                                    attr='browse',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='to_unlink_candidate_ids', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='move_to_recompute_state', ctx=Load()),
                                            attr='_recompute_state',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_aggregated_product_quantities',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Returns a dictionary of products (key = id+name+description+uom) and corresponding values of interest.\n\n        Allows aggregation of data across separate move lines for the same product. This is expected to be useful\n        in things such as delivery reports. Dict key is made as a combination of values we expect to want to group\n        the products by (i.e. so data is not lost). This function purposely ignores lots/SNs because these are\n        expected to already be properly grouped by line.\n\n        returns: dictionary {product_id+name+description+uom: {product, name, description, qty_done, product_uom}, ...}\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='aggregated_move_lines', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        FunctionDef(
                            name='get_aggregated_properties',
                            args=arguments(
                                posonlyargs=[],
                                args=[
                                    arg(arg='move_line', annotation=None, type_comment=None),
                                    arg(arg='move', annotation=None, type_comment=None),
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
                                    targets=[Name(id='move', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            Name(id='move', ctx=Load()),
                                            Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='move_id',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='uom', ctx=Store())],
                                    value=BoolOp(
                                        op=Or(),
                                        values=[
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='move_line', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='product_uom_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Attribute(
                                                value=Name(id='move', ctx=Load()),
                                                attr='product_uom',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='move', ctx=Load()),
                                            attr='product_id',
                                            ctx=Load(),
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='description', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='description_picking',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Compare(
                                                left=Name(id='description', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Name(id='name', ctx=Load())],
                                            ),
                                            Compare(
                                                left=Name(id='description', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='move', ctx=Load()),
                                                            attr='product_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='description', ctx=Store())],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='product', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='move', ctx=Load()),
                                        attr='product_id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='line_key', ctx=Store())],
                                    value=JoinedStr(
                                        values=[
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='_', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='product', ctx=Load()),
                                                    attr='display_name',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='_', kind=None),
                                            FormattedValue(
                                                value=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='description', ctx=Load()),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                            Constant(value='_', kind=None),
                                            FormattedValue(
                                                value=Attribute(
                                                    value=Name(id='uom', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                conversion=-1,
                                                format_spec=None,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Tuple(
                                        elts=[
                                            Name(id='line_key', ctx=Load()),
                                            Name(id='name', ctx=Load()),
                                            Name(id='description', ctx=Load()),
                                            Name(id='uom', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='backorders', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='stock.picking', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pickings', ctx=Store())],
                            value=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='picking_id',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        While(
                            test=Attribute(
                                value=Name(id='pickings', ctx=Load()),
                                attr='backorder_ids',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='backorders', ctx=Store()),
                                    op=BitOr(),
                                    value=Attribute(
                                        value=Name(id='pickings', ctx=Load()),
                                        attr='backorder_ids',
                                        ctx=Load(),
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='pickings', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='pickings', ctx=Load()),
                                        attr='backorder_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='move_line', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='line_key', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                                Name(id='description', ctx=Store()),
                                                Name(id='uom', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='get_aggregated_properties', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move_line',
                                                value=Name(id='move_line', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='line_key', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='aggregated_move_lines', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_ordered', ctx=Store())],
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='move_line', ctx=Load()),
                                                    attr='move_id',
                                                    ctx=Load(),
                                                ),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='backorders', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='following_move_lines', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='backorders', ctx=Load()),
                                                                attr='move_line_ids',
                                                                ctx=Load(),
                                                            ),
                                                            attr='filtered',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Lambda(
                                                                args=arguments(
                                                                    posonlyargs=[],
                                                                    args=[arg(arg='ml', annotation=None, type_comment=None)],
                                                                    vararg=None,
                                                                    kwonlyargs=[],
                                                                    kw_defaults=[],
                                                                    kwarg=None,
                                                                    defaults=[],
                                                                ),
                                                                body=Compare(
                                                                    left=Subscript(
                                                                        value=Call(
                                                                            func=Name(id='get_aggregated_properties', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='move',
                                                                                    value=Attribute(
                                                                                        value=Name(id='ml', ctx=Load()),
                                                                                        attr='move_id',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        slice=Constant(value=0, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    ops=[Eq()],
                                                                    comparators=[Name(id='line_key', ctx=Load())],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                AugAssign(
                                                    target=Name(id='qty_ordered', ctx=Store()),
                                                    op=Add(),
                                                    value=Call(
                                                        func=Name(id='sum', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='following_move_lines', ctx=Load()),
                                                                        attr='move_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='mapped',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='product_uom_qty', kind=None)],
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
                                            targets=[
                                                Subscript(
                                                    value=Name(id='aggregated_move_lines', ctx=Load()),
                                                    slice=Name(id='line_key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='description', kind=None),
                                                    Constant(value='qty_done', kind=None),
                                                    Constant(value='qty_ordered', kind=None),
                                                    Constant(value='product_uom', kind=None),
                                                    Constant(value='product', kind=None),
                                                ],
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='description', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='qty_done',
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='qty_ordered', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='uom', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='move_line', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='aggregated_move_lines', ctx=Load()),
                                                    slice=Name(id='line_key', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='qty_done', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Attribute(
                                                value=Name(id='move_line', ctx=Load()),
                                                attr='qty_done',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='pickings', ctx=Store())],
                            value=BinOp(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='picking_id',
                                    ctx=Load(),
                                ),
                                op=BitOr(),
                                right=Name(id='backorders', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='empty_move', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='pickings', ctx=Load()),
                                        attr='move_lines',
                                        ctx=Load(),
                                    ),
                                    attr='filtered',
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
                                        body=BoolOp(
                                            op=And(),
                                            values=[
                                                Compare(
                                                    left=Attribute(
                                                        value=Name(id='m', ctx=Load()),
                                                        attr='state',
                                                        ctx=Load(),
                                                    ),
                                                    ops=[Eq()],
                                                    comparators=[Constant(value='cancel', kind=None)],
                                                ),
                                                Attribute(
                                                    value=Name(id='m', ctx=Load()),
                                                    attr='product_uom_qty',
                                                    ctx=Load(),
                                                ),
                                                Call(
                                                    func=Name(id='float_is_zero', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='m', ctx=Load()),
                                                            attr='quantity_done',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[
                                                        keyword(
                                                            arg='precision_rounding',
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='m', ctx=Load()),
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
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='line_key', ctx=Store()),
                                                Name(id='name', ctx=Store()),
                                                Name(id='description', ctx=Store()),
                                                Name(id='uom', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='get_aggregated_properties', ctx=Load()),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='move',
                                                value=Name(id='empty_move', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='line_key', ctx=Load()),
                                        ops=[NotIn()],
                                        comparators=[Name(id='aggregated_move_lines', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='qty_ordered', ctx=Store())],
                                            value=Attribute(
                                                value=Name(id='empty_move', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='aggregated_move_lines', ctx=Load()),
                                                    slice=Name(id='line_key', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='description', kind=None),
                                                    Constant(value='qty_done', kind=None),
                                                    Constant(value='qty_ordered', kind=None),
                                                    Constant(value='product_uom', kind=None),
                                                    Constant(value='product', kind=None),
                                                ],
                                                values=[
                                                    Name(id='name', ctx=Load()),
                                                    Name(id='description', ctx=Load()),
                                                    Constant(value=False, kind=None),
                                                    Name(id='qty_ordered', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='uom', ctx=Load()),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='empty_move', ctx=Load()),
                                                        attr='product_id',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        AugAssign(
                                            target=Subscript(
                                                value=Subscript(
                                                    value=Name(id='aggregated_move_lines', ctx=Load()),
                                                    slice=Name(id='line_key', ctx=Load()),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='qty_ordered', kind=None),
                                                ctx=Store(),
                                            ),
                                            op=Add(),
                                            value=Attribute(
                                                value=Name(id='empty_move', ctx=Load()),
                                                attr='product_uom_qty',
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='aggregated_move_lines', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_sale_price',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[Pass()],
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
