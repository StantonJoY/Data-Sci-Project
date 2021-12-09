Module(
    body=[
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='IntegrityError', asname=None)],
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
            module='odoo.tests',
            names=[alias(name='tagged', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestProductAttributeValueCommon',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='setUpClass',
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
                                            Name(id='TestProductAttributeValueCommon', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='setUpClass',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='price', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Super Computer', kind=None),
                                            Constant(value=2000, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_ssd_attribute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_ram_attribute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_hdd_attribute',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer_case',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Super Computer Case', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_size_attribute',
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
                    name='_add_ssd_attribute',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ssd_attribute',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Memory', kind=None),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ssd_256',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='256 GB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ssd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ssd_512',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='512 GB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ssd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_ssd_attribute_line',
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
                    name='_add_ssd_attribute_line',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer_ssd_attribute_lines',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ssd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='ssd_256',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='ssd_512',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_ssd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=200, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_ssd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=400, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_ram_attribute',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ram_attribute',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='RAM', kind=None),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ram_8',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='8 GB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ram_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ram_16',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='16 GB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ram_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='ram_32',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='32 GB', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ram_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer_ram_attribute_lines',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='ram_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='ram_8',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='ram_16',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='ram_32',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_ram_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=20, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_ram_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=40, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_ram_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=80, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_hdd_attribute',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='hdd_attribute',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='HDD', kind=None),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='hdd_1',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='1 To', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='hdd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='hdd_2',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='2 To', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='hdd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='hdd_4',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='4 To', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='hdd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='_add_hdd_attribute_line',
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
                    name='_add_hdd_attribute_line',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer_hdd_attribute_lines',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='hdd_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='hdd_1',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='hdd_2',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='hdd_4',
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_hdd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_hdd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=4, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='cls', ctx=Load()),
                                                attr='computer_hdd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=2, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='price_extra',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=8, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_add_ram_exclude_for',
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
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_product_value_id',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer_ram_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ram_16',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='exclude_for', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='computer',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Call(
                                                                                                    func=Attribute(
                                                                                                        value=Name(id='self', ctx=Load()),
                                                                                                        attr='_get_product_value_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    args=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='computer_hdd_attribute_lines',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Attribute(
                                                                                                            value=Name(id='self', ctx=Load()),
                                                                                                            attr='hdd_1',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ],
                                                                                                    keywords=[],
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
                    name='_add_size_attribute',
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
                            targets=[
                                Attribute(
                                    value=Name(id='cls', ctx=Load()),
                                    attr='size_attribute',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Size', kind=None),
                                            Constant(value=4, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='size_m',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='M', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='size_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=1, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='size_l',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='L', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='size_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=2, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='size_xl',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='sequence', kind=None),
                                        ],
                                        values=[
                                            Constant(value='XL', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='size_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value=3, kind=None),
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
                                    value=Name(id='cls', ctx=Load()),
                                    attr='computer_case_size_attribute_lines',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='cls', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='computer_case',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='cls', ctx=Load()),
                                                    attr='size_attribute',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='size_m',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='size_l',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='cls', ctx=Load()),
                                                                            attr='size_xl',
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
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_product_value_id',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_template_attribute_lines', annotation=None, type_comment=None),
                            arg(arg='product_attribute_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Attribute(
                                            value=Name(id='product_template_attribute_lines', ctx=Load()),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        attr='filtered',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='product_value_id', annotation=None, type_comment=None)],
                                                vararg=None,
                                                kwonlyargs=[],
                                                kw_defaults=[],
                                                kwarg=None,
                                                defaults=[],
                                            ),
                                            body=Compare(
                                                left=Attribute(
                                                    value=Name(id='product_value_id', ctx=Load()),
                                                    attr='product_attribute_value_id',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Name(id='product_attribute_value', ctx=Load())],
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Constant(value=0, kind=None),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_product_template_attribute_value',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='product_attribute_value', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='\n            Return the `product.template.attribute.value` matching\n                `product_attribute_value` for self.\n\n            :param: recordset of one product.attribute.value\n            :return: recordset of one product.template.attribute.value if found\n                else empty\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='model', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='model', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='model', ctx=Load()),
                                                    attr='valid_product_template_attribute_line_ids',
                                                    ctx=Load(),
                                                ),
                                                attr='filtered',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Lambda(
                                                    args=arguments(
                                                        posonlyargs=[],
                                                        args=[arg(arg='l', annotation=None, type_comment=None)],
                                                        vararg=None,
                                                        kwonlyargs=[],
                                                        kw_defaults=[],
                                                        kwarg=None,
                                                        defaults=[],
                                                    ),
                                                    body=Compare(
                                                        left=Attribute(
                                                            value=Name(id='l', ctx=Load()),
                                                            attr='attribute_id',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='product_attribute_value', ctx=Load()),
                                                                attr='attribute_id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='product_template_value_ids',
                                        ctx=Load(),
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
                                            left=Attribute(
                                                value=Name(id='v', ctx=Load()),
                                                attr='product_attribute_value_id',
                                                ctx=Load(),
                                            ),
                                            ops=[Eq()],
                                            comparators=[Name(id='product_attribute_value', ctx=Load())],
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
                    name='_add_exclude',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='m1', annotation=None, type_comment=None),
                            arg(arg='m2', annotation=None, type_comment=None),
                            arg(arg='product_template', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='m1', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='exclude_for', kind=None)],
                                        values=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=0, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='product_tmpl_id', kind=None),
                                                                    Constant(value='value_ids', kind=None),
                                                                ],
                                                                values=[
                                                                    Attribute(
                                                                        value=BoolOp(
                                                                            op=Or(),
                                                                            values=[
                                                                                Name(id='product_template', ctx=Load()),
                                                                                Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='computer',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    List(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Constant(value=6, kind=None),
                                                                                    Constant(value=0, kind=None),
                                                                                    List(
                                                                                        elts=[
                                                                                            Attribute(
                                                                                                value=Name(id='m2', ctx=Load()),
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
            name='TestProductAttributeValueConfig',
            bases=[Name(id='TestProductAttributeValueCommon', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_product_template_attribute_values_creation',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer_ssd_attribute_lines',
                                                    ctx=Load(),
                                                ),
                                                attr='product_template_value_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                    Constant(value='Product attribute values (ssd) were not automatically created', kind=None),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer_ram_attribute_lines',
                                                    ctx=Load(),
                                                ),
                                                attr='product_template_value_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='Product attribute values (ram) were not automatically created', kind=None),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer_hdd_attribute_lines',
                                                    ctx=Load(),
                                                ),
                                                attr='product_template_value_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='Product attribute values (hdd) were not automatically created', kind=None),
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer_case_size_attribute_lines',
                                                    ctx=Load(),
                                                ),
                                                attr='product_template_value_ids',
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=3, kind=None),
                                    Constant(value='Product attribute values (size) were not automatically created', kind=None),
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
                    name='test_get_variant_for_combination',
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
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_16', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_16',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                    op=Add(),
                                    right=Name(id='computer_ram_8', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='computer_hdd_1', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ok_variant', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[Name(id='combination', ctx=Load())],
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
                                    Attribute(
                                        value=Name(id='ok_variant', ctx=Load()),
                                        attr='product_template_attribute_value_ids',
                                        ctx=Load(),
                                    ),
                                    Name(id='combination', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=Name(id='computer_ssd_256', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='computer_ram_8', ctx=Load()),
                                    ),
                                    op=Add(),
                                    right=Name(id='computer_ram_16', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='computer_hdd_1', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='variant', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[Name(id='combination', ctx=Load())],
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
                                        args=[Name(id='variant', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Constant(value=0, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=BinOp(
                                left=Name(id='computer_ssd_256', ctx=Load()),
                                op=Add(),
                                right=Name(id='computer_ram_8', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='variant', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[Name(id='combination', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[Name(id='variant', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_product_filtered_exclude_for',
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
                            value=Constant(value='\n            Super Computer has 18 variants total (2 ssd * 3 ram * 3 hdd)\n            RAM 16 excudes HDD 1, that matches 2 variants:\n            - SSD 256 RAM 16 HDD 1\n            - SSD 512 RAM 16 HDD 1\n\n            => There has to be 16 variants left when filtered\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ssd_512', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_512',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_16', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_16',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_possible_variants',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=18, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_ram_exclude_for',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_possible_variants',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=16, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_variant_for_combination',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='computer_ram_8', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_is_variant_possible',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_variant_for_combination',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='computer_ram_16', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_is_variant_possible',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_variant_for_combination',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=BinOp(
                                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                                            op=Add(),
                                                            right=Name(id='computer_ram_16', ctx=Load()),
                                                        ),
                                                        op=Add(),
                                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='_is_variant_possible',
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
                    name='test_children_product_filtered_exclude_for',
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
                            value=Constant(value='\n            Super Computer Case has 3 variants total (3 size)\n            Reference product Computer with HDD 4 excludes Size M\n            The following variant will be excluded:\n            - Size M\n\n            => There has to be 2 variants left when filtered\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_4',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_size_m', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='size_m',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer_case',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_hdd_4', ctx=Load()),
                                    Name(id='computer_size_m', ctx=Load()),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer_case',
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
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer_case',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_possible_variants',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='computer_hdd_4', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    Constant(value=2, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer_case',
                                                        ctx=Load(),
                                                    ),
                                                    attr='_get_variant_for_combination',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='computer_size_m', ctx=Load())],
                                                keywords=[],
                                            ),
                                            attr='_is_variant_possible',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='computer_hdd_4', ctx=Load())],
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
                    name='test_is_combination_possible',
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
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_16', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_16',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_16', ctx=Load()),
                                    Name(id='computer_hdd_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_16', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='computer_ssd_256', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='computer_ram_16', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mouse', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Mouse', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.template.attribute.value', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='color_attribute', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Color', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='color_red', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Red', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                            targets=[Name(id='color_green', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Green', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='mouse', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='color_red', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='color_green', ctx=Load()),
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
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mouse_color_red', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='color_red', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mouse_color_green', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='color_green', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ssd_256', ctx=Load()),
                                    Name(id='mouse_color_green', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='variant', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_16', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='mouse_color_red', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                            Name(id='mouse_color_red', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='mouse_color_red', ctx=Load()),
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                            Name(id='mouse_color_green', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='mouse_color_green', ctx=Load()),
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='variant', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                    op=Add(),
                                    right=Name(id='computer_ram_8', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='computer_hdd_1', ctx=Load()),
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
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_template_attribute_value_ids', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='combination', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
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
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.product', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_template_attribute_value_ids', kind=None),
                                            Constant(value='active', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='combination', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value=True, kind=None),
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
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                                    op=Add(),
                                                    right=Name(id='computer_ram_8', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_1', ctx=Load()),
                                            ),
                                        ],
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
                    name='test_get_first_possible_combination',
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
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ssd_512', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_512',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_16', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_16',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_32', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_32',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_2',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_4',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_16', ctx=Load()),
                                    Name(id='computer_hdd_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='gen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_possible_combinations',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='gen', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_16', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_attribute',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=10, kind=None),
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_attribute',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_16', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_32', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
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
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_32', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=3, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_16', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_16', ctx=Load()),
                                    Name(id='computer_hdd_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_16', ctx=Load()),
                                    Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='computer_ram_16', ctx=Load()),
                                        attr='product_attribute_value_id',
                                        ctx=Load(),
                                    ),
                                    attr='sequence',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=2, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_8', ctx=Load()),
                                    Name(id='computer_hdd_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_8', ctx=Load()),
                                    Name(id='computer_hdd_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_8', ctx=Load()),
                                    Name(id='computer_hdd_4', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_32', ctx=Load()),
                                    Name(id='computer_hdd_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_32', ctx=Load()),
                                    Name(id='computer_hdd_2', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_32', ctx=Load()),
                                    Name(id='computer_ssd_256', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_32', ctx=Load()),
                                    Name(id='computer_hdd_4', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='gen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_possible_combinations',
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
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='gen', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mouse', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Mouse', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_is_combination_possible',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.template.attribute.value', kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='color_attribute', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='Color', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='color_red', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Red', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                            targets=[Name(id='color_green', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Green', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='mouse', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='color_red', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='color_green', ctx=Load()),
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
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mouse_color_red', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='color_red', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='mouse_color_green', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='color_green', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ssd_256', ctx=Load()),
                                    Name(id='mouse_color_red', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='parent_combination',
                                                value=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='computer_ssd_256', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='computer_ram_8', ctx=Load()),
                                                    ),
                                                    op=Add(),
                                                    right=Name(id='computer_hdd_1', ctx=Load()),
                                                ),
                                            ),
                                        ],
                                    ),
                                    Name(id='mouse_color_green', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='color_blue', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Blue', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                            targets=[Name(id='color_yellow', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.attribute.value', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                        ],
                                        values=[
                                            Constant(value='Yellow', kind=None),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='product.template.attribute.line', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='attribute_id', kind=None),
                                            Constant(value='value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Name(id='mouse', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='color_attribute', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            List(
                                                                elts=[
                                                                    Attribute(
                                                                        value=Name(id='color_blue', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='color_yellow', ctx=Load()),
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
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mouse_color_yellow', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='color_yellow', ctx=Load()),
                                    Name(id='mouse', ctx=Load()),
                                ],
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
                                        func=Attribute(
                                            value=Name(id='mouse', ctx=Load()),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='necessary_values',
                                                value=Name(id='mouse_color_yellow', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    BinOp(
                                        left=Name(id='mouse_color_red', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='mouse_color_yellow', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='many combinations', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product_attribute', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.attribute', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='att %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                    Constant(value='dynamic', kind=None),
                                                    Name(id='i', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='j', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=50, kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='product.attribute.value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='attribute_id', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='val %s', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='j', ctx=Load()),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='product_attribute', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='j', ctx=Load()),
                                                                ],
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
                                                slice=Constant(value='product.template.attribute.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='attribute_id', kind=None),
                                                            Constant(value='product_tmpl_id', kind=None),
                                                            Constant(value='value_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='product_attribute', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product_template', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=6, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='product_attribute', ctx=Load()),
                                                                                    attr='value_ids',
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
                                                        ],
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
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_product_template_attribute_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='attribute_line_ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Name(id='product_template', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_product_template_attribute_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='attribute_line_ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Name(id='product_template', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='product_template', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_product_template_attribute_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='attribute_line_ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Name(id='product_template', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_product_template_attribute_value',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='product_template', ctx=Load()),
                                                            attr='attribute_line_ids',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=1, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=1, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='model',
                                                value=Name(id='product_template', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    Name(id='product_template', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.template.attribute.value', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='idx', ctx=Store()),
                                    Name(id='ptal', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Name(id='enumerate', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='product_template', ctx=Load()),
                                        attr='attribute_line_ids',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='idx', ctx=Load()),
                                        ops=[NotEq()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='ptal', ctx=Load()),
                                                    attr='product_template_value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[Name(id='value', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='ptal', ctx=Load()),
                                                    attr='product_template_value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=2, kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                                AugAssign(
                                    target=Name(id='combination', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='value', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='started_at', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='_get_first_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Name(id='combination', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='elapsed', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='time',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='started_at', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='elapsed', ctx=Load()),
                                    Constant(value=0.5, kind=None),
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
                    name='test_get_closest_possible_combinations',
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
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ssd_512', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_512',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_16', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_16',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_32', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_32',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_2', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_2',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_4', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_4',
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_add_exclude',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='computer_ram_16', ctx=Load()),
                                    Name(id='computer_hdd_1', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='gen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_possible_combinations',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=None, kind=None)],
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
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='gen', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_closest_possible_combinations',
                                    ctx=Load(),
                                ),
                                args=[Name(id='computer_hdd_1', ctx=Load())],
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
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[Name(id='gen', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_512', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_32', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIsNone',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='next', ctx=Load()),
                                        args=[
                                            Name(id='gen', ctx=Load()),
                                            Constant(value=None, kind=None),
                                        ],
                                        keywords=[],
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='computer_hdd_2', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='computer_hdd_2', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='computer_ram_16', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_16', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_2', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Name(id='computer_hdd_1', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='computer_ram_16', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_1', ctx=Load()),
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
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_closest_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=Name(id='computer_ssd_256', ctx=Load()),
                                                        op=Add(),
                                                        right=Name(id='computer_ram_8', ctx=Load()),
                                                    ),
                                                    op=Add(),
                                                    right=Name(id='computer_hdd_4', ctx=Load()),
                                                ),
                                                op=Add(),
                                                right=Name(id='computer_hdd_2', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=BinOp(
                                            left=Name(id='computer_ssd_256', ctx=Load()),
                                            op=Add(),
                                            right=Name(id='computer_ram_8', ctx=Load()),
                                        ),
                                        op=Add(),
                                        right=Name(id='computer_hdd_4', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='name', kind=None)],
                                        values=[Constant(value='many combinations', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[Constant(value=10, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product_attribute', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='product.attribute', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='create_variant', kind=None),
                                                    Constant(value='sequence', kind=None),
                                                ],
                                                values=[
                                                    BinOp(
                                                        left=Constant(value='att %s', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                    Constant(value='dynamic', kind=None),
                                                    Name(id='i', ctx=Load()),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='j', ctx=Store()),
                                    iter=Call(
                                        func=Name(id='range', ctx=Load()),
                                        args=[Constant(value=10, kind=None)],
                                        keywords=[],
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
                                                        slice=Constant(value='product.attribute.value', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Dict(
                                                                keys=[
                                                                    Constant(value='name', kind=None),
                                                                    Constant(value='attribute_id', kind=None),
                                                                    Constant(value='sequence', kind=None),
                                                                ],
                                                                values=[
                                                                    BinOp(
                                                                        left=Constant(value='val %s/%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Tuple(
                                                                            elts=[
                                                                                Name(id='i', ctx=Load()),
                                                                                Name(id='j', ctx=Load()),
                                                                            ],
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='product_attribute', ctx=Load()),
                                                                        attr='id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='j', ctx=Load()),
                                                                ],
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
                                                slice=Constant(value='product.template.attribute.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Dict(
                                                        keys=[
                                                            Constant(value='attribute_id', kind=None),
                                                            Constant(value='product_tmpl_id', kind=None),
                                                            Constant(value='value_ids', kind=None),
                                                        ],
                                                        values=[
                                                            Attribute(
                                                                value=Name(id='product_attribute', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            Attribute(
                                                                value=Name(id='product_template', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            List(
                                                                elts=[
                                                                    Tuple(
                                                                        elts=[
                                                                            Constant(value=6, kind=None),
                                                                            Constant(value=0, kind=None),
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='product_attribute', ctx=Load()),
                                                                                    attr='value_ids',
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
                                                        ],
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='product.template.attribute.value', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ptal', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='product_template', ctx=Load()),
                                attr='attribute_line_ids',
                                ctx=Load(),
                            ),
                            body=[
                                AugAssign(
                                    target=Name(id='combination', ctx=Store()),
                                    op=Add(),
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='ptal', ctx=Load()),
                                            attr='product_template_value_ids',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=5, kind=None),
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='started_at', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='time', ctx=Load()),
                                    attr='time',
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
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='product_template', ctx=Load()),
                                            attr='_get_closest_possible_combination',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='combination', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Name(id='combination', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='elapsed', ctx=Store())],
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='time', ctx=Load()),
                                        attr='time',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Sub(),
                                right=Name(id='started_at', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertLess',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='elapsed', ctx=Load()),
                                    Constant(value=0.5, kind=None),
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
                    name='test_clear_caches',
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
                            value=Constant(value='The goal of this test is to make sure the cache is invalidated when\n        it should be.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='computer_ssd_256', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ssd_256',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_ram_8', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ram_8',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='computer_hdd_1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_product_template_attribute_value',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='combination', ctx=Store())],
                            value=BinOp(
                                left=BinOp(
                                    left=Name(id='computer_ssd_256', ctx=Load()),
                                    op=Add(),
                                    right=Name(id='computer_ram_8', ctx=Load()),
                                ),
                                op=Add(),
                                right=Name(id='computer_hdd_1', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='variant', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='computer',
                                        ctx=Load(),
                                    ),
                                    attr='_get_variant_for_combination',
                                    ctx=Load(),
                                ),
                                args=[Name(id='combination', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[Name(id='variant', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='variant', ctx=Load()),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='combination', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='variant', ctx=Store())],
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
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='product_tmpl_id', kind=None),
                                            Constant(value='product_template_attribute_value_ids', kind=None),
                                        ],
                                        values=[
                                            Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='computer',
                                                    ctx=Load(),
                                                ),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value=6, kind=None),
                                                            Constant(value=0, kind=None),
                                                            Attribute(
                                                                value=Name(id='combination', ctx=Load()),
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
                                    ),
                                ],
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
                                    Name(id='variant', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='combination', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='variant', ctx=Load()),
                                    attr='product_template_attribute_value_ids',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertFalse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer',
                                                ctx=Load(),
                                            ),
                                            attr='_get_variant_id_for_combination',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='combination', ctx=Load())],
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
                    name='test_constraints',
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
                            value=Constant(value='The goal of this test is to make sure constraints are correct.', kind=None),
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change variants creation mode of attribute used on product", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ram_attribute',
                                                ctx=Load(),
                                            ),
                                            attr='create_variant',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='no_variant', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't delete attribute used on product", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ram_attribute',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change the attribute of an value used on product", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ram_32',
                                                ctx=Load(),
                                            ),
                                            attr='attribute_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='hdd_attribute',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't delete value used on product", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='ram_32',
                                                ctx=Load(),
                                            ),
                                            attr='unlink',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't have attribute without value on product", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                slice=Constant(value='product.template.attribute.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='attribute_id', kind=None),
                                                    Constant(value='value_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='computer_case',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='hdd_attribute',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    List(elts=[], ctx=Load()),
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
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='ValidationError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value='value attribute must match line attribute', kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                slice=Constant(value='product.template.attribute.line', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='product_tmpl_id', kind=None),
                                                    Constant(value='attribute_id', kind=None),
                                                    Constant(value='value_ids', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='computer_case',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='ram_attribute',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    List(
                                                        elts=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=6, kind=None),
                                                                    Constant(value=0, kind=None),
                                                                    List(
                                                                        elts=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='self', ctx=Load()),
                                                                                    attr='ssd_256',
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
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change the attribute of an attribute line", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer_ssd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='attribute_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='hdd_attribute',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change the product of an attribute line", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='computer_ssd_attribute_lines',
                                                ctx=Load(),
                                            ),
                                            attr='product_tmpl_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='computer_case',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change the value of a product template attribute value", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer_ram_attribute_lines',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_template_value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='product_attribute_value_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='hdd_1',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='UserError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't change the product of a product template attribute value", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='computer_ram_attribute_lines',
                                                        ctx=Load(),
                                                    ),
                                                    attr='product_template_value_ids',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='product_tmpl_id',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='computer_case',
                                            ctx=Load(),
                                        ),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            type_comment=None,
                        ),
                        With(
                            items=[
                                withitem(
                                    context_expr=Call(
                                        func=Name(id='mute_logger', ctx=Load()),
                                        args=[Constant(value='odoo.sql_db', kind=None)],
                                        keywords=[],
                                    ),
                                    optional_vars=None,
                                ),
                                withitem(
                                    context_expr=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertRaises',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='IntegrityError', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='msg',
                                                value=Constant(value="can't have two values with the same name for the same attribute", kind=None),
                                            ),
                                        ],
                                    ),
                                    optional_vars=None,
                                ),
                            ],
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
                                                slice=Constant(value='product.attribute.value', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='attribute_id', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='32 GB', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='ram_attribute',
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
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
