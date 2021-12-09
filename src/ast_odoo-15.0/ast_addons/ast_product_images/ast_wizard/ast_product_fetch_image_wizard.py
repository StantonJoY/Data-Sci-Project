Module(
    body=[
        Import(
            names=[alias(name='base64', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[alias(name='timedelta', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ImportFrom(
            module='requests.exceptions',
            names=[alias(name='ConnectionError', asname='RequestConnectionError')],
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
            names=[alias(name='UserError', asname=None)],
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
            name='ProductFetchImageWizard',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='TransientModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='product.fetch.image.wizard', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value="Fetch product images from Google Images based on the product's barcode number.", kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_session', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='requests', ctx=Load()),
                            attr='Session',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
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
                            targets=[Name(id='ir_cron_fetch_image', ctx=Store())],
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
                                args=[Constant(value='product_images.ir_cron_fetch_image', kind=None)],
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
                                operand=Name(id='ir_cron_fetch_image', ctx=Load()),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The scheduled action "Product Images: Get product images from Google" has been deleted. Please contact your administrator to have the action restored or to reinstall the module "product_images".', kind=None)],
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
                            targets=[Name(id='cron_triggers_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.cron.trigger', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search_count',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='cron_id', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Attribute(
                                                        value=Name(id='ir_cron_fetch_image', ctx=Load()),
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
                        If(
                            test=Compare(
                                left=Name(id='cron_triggers_count', ctx=Load()),
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
                                                args=[Constant(value='A task to process products in the background is already running. Please try againlater.', kind=None)],
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
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.config_parameter', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_pse_id_is_set', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ICP', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='google.pse.id', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='google_custom_search_key_is_set', ctx=Store())],
                            value=Call(
                                func=Name(id='bool', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='ICP', ctx=Load()),
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='google.custom_search.key', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='google_pse_id_is_set', ctx=Load()),
                                        Name(id='google_custom_search_key_is_set', ctx=Load()),
                                    ],
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The API Key and Search Engine ID must be set in the General Settings.', kind=None)],
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
                            test=Compare(
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
                                    args=[Constant(value='active_model', kind=None)],
                                    keywords=[],
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='product.template', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='product_ids', ctx=Store())],
                                    value=Attribute(
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
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='_context',
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='active_ids', kind=None)],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='product_variant_ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='product_ids', ctx=Store())],
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
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_context',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='active_ids', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='nb_products_selected', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='product_ids', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='products_to_process', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='product_ids', ctx=Load()),
                                    attr='filtered',
                                    ctx=Load(),
                                ),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='p', annotation=None, type_comment=None)],
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
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='image_1920',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                Attribute(
                                                    value=Name(id='p', ctx=Load()),
                                                    attr='barcode',
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
                            targets=[Name(id='nb_products_to_process', ctx=Store())],
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='products_to_process', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nb_products_unable_to_process', ctx=Store())],
                            value=BinOp(
                                left=Name(id='nb_products_selected', ctx=Load()),
                                op=Sub(),
                                right=Name(id='nb_products_to_process', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='defaults', ctx=Store())],
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
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='defaults', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='products_to_process',
                                        value=Name(id='products_to_process', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nb_products_selected',
                                        value=Name(id='nb_products_selected', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nb_products_to_process',
                                        value=Name(id='nb_products_to_process', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='nb_products_unable_to_process',
                                        value=Name(id='nb_products_unable_to_process', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='defaults', ctx=Load()),
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
                    targets=[Name(id='nb_products_selected', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Number of selected products', kind=None),
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
                    targets=[Name(id='products_to_process', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='comodel_name',
                                value=Constant(value='product.product', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The list of selected products that meet the criteria (have a barcode and no image)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='nb_products_to_process', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Number of products to process', kind=None),
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
                    targets=[Name(id='nb_products_unable_to_process', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Number of product unprocessable', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_fetch_image',
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
                            value=Constant(value=' Fetch the images of the first ten products and delegate the remaining to the cron.\n\n        The first ten images are immediately fetched to improve the user experience. This way, they\n        can immediately browse the processed products and be assured that the task is running well.\n        Also, if any error occurs, it can be thrown to the user. Then, a cron job is triggered to be\n        run as soon as possible, unless the daily request limit has been reached. In that case, the\n        cron job is scheduled to run a day later.\n\n        :return: A notification to inform the user about the outcome of the action\n        :rtype: dict\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='products_to_process',
                                        ctx=Load(),
                                    ),
                                    attr='image_fetch_pending',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=True, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='matching_images_count', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_products',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_products_to_process',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=10, kind=None)],
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_products_to_process',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='ir_cron_fetch_image', ctx=Store())],
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
                                        args=[Constant(value='product_images.ir_cron_fetch_image', kind=None)],
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
                                        operand=Name(id='ir_cron_fetch_image', ctx=Load()),
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The scheduled action "Product Images: Get product images from Google" has been deleted. Please contact your administrator to have the action restored or to reinstall the module "product_images".', kind=None)],
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
                                    targets=[Name(id='cron_triggers_count', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.cron.trigger', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search_count',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='cron_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='ir_cron_fetch_image', ctx=Load()),
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
                                If(
                                    test=Compare(
                                        left=Name(id='cron_triggers_count', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
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
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='automatically_triggered',
                                                                value=Constant(value=False, kind=None),
                                                            ),
                                                        ],
                                                    ),
                                                    attr='_trigger_fetch_images_cron',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Products are processed in the background. Images will be updated progressively.', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='warning_type', ctx=Store())],
                                    value=Constant(value='success', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='%(matching_images_count)s matching images have been found for %(product_count)s products.', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='matching_images_count',
                                                value=Name(id='matching_images_count', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='product_count',
                                                value=Call(
                                                    func=Name(id='len', ctx=Load()),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='products_to_process',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='warning_type', ctx=Store())],
                                    value=IfExp(
                                        test=Compare(
                                            left=Name(id='matching_images_count', ctx=Load()),
                                            ops=[Gt()],
                                            comparators=[Constant(value=0, kind=None)],
                                        ),
                                        body=Constant(value='success', kind=None),
                                        orelse=Constant(value='warning', kind=None),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='tag', kind=None),
                                    Constant(value='params', kind=None),
                                ],
                                values=[
                                    Constant(value='ir.actions.client', kind=None),
                                    Constant(value='display_notification', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='title', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='message', kind=None),
                                            Constant(value='next', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Product images', kind=None)],
                                                keywords=[],
                                            ),
                                            Name(id='warning_type', ctx=Load()),
                                            Name(id='message', ctx=Load()),
                                            Dict(
                                                keys=[Constant(value='type', kind=None)],
                                                values=[Constant(value='ir.actions.act_window_close', kind=None)],
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
                    name='_cron_fetch_image',
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
                            value=Constant(value=' Fetch images of a list of products using their barcode.\n\n        This method is called from a cron job. If the daily request limit is reached, the cron job\n        is scheduled to run again a day later.\n\n        :return: None\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_process_products',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_products_to_process',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value=100, kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_products_to_process',
                                    ctx=Load(),
                                ),
                                args=[Constant(value=1, kind=None)],
                                keywords=[],
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
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='automatically_triggered',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='_trigger_fetch_images_cron',
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
                                                        attr='now',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='timedelta', ctx=Load()),
                                                    args=[],
                                                    keywords=[
                                                        keyword(
                                                            arg='minutes',
                                                            value=Constant(value=1.0, kind=None),
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
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_products_to_process',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='limit', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=10000, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Get the products that need to be processed and meet the criteria.\n\n        The criteria are to have a barcode and no image. If `products_to_process` is not populated,\n        the DB is searched to find matching product records.\n\n        :param int limit: The maximum number of records to return, defaulting to 10000 to match\n                          Google's API default rate limit\n        :return: The products that meet the criteria\n        :rtype: recordset of `product.product`\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='products_to_process', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='products_to_process',
                                        ctx=Load(),
                                    ),
                                    Call(
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
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='image_fetch_pending', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value=True, kind=None),
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
                                                value=Name(id='limit', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='products_to_process', ctx=Load()),
                                        attr='filtered',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Lambda(
                                            args=arguments(
                                                posonlyargs=[],
                                                args=[arg(arg='p', annotation=None, type_comment=None)],
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
                                                            value=Name(id='p', ctx=Load()),
                                                            attr='image_1920',
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='barcode',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='p', ctx=Load()),
                                                        attr='image_fetch_pending',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                slice=Slice(
                                    lower=None,
                                    upper=Name(id='limit', ctx=Load()),
                                    step=None,
                                ),
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_process_products',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='products_to_process', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Fetch an image from the Google Custom Search API for each product.\n\n        We fetch the 10 first image URLs and save the first valid image.\n\n        :param recordset products_to_process: The products for which an image must be fetched, as a\n                                              `product.product` recordset\n        :return: The number of products for which a matching image was found\n        :rtype: int\n        :raises UserError: If the project is misconfigured on Google's side\n        :raises UserError: If the API Key or Search Engine ID is incorrect\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='products_to_process', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Constant(value=0, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='nb_service_unavailable_codes', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='nb_timeouts', ctx=Store())],
                            value=Constant(value=0, kind=None),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='product', ctx=Store()),
                            iter=Name(id='products_to_process', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_fetch_image_urls_from_google',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='product', ctx=Load()),
                                                        attr='barcode',
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
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='requests', ctx=Load()),
                                                            attr='codes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='forbidden',
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
                                                                args=[Constant(value='The Custom Search API is not enabled in your Google project. Please visit your Google Cloud Platform project page and enable it, then retry. If you enabled this API recently, please wait a few minutes and retry.', kind=None)],
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
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='status_code',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='requests', ctx=Load()),
                                                                    attr='codes',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='service_unavailable',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        AugAssign(
                                                            target=Name(id='nb_service_unavailable_codes', ctx=Store()),
                                                            op=Add(),
                                                            value=Constant(value=1, kind=None),
                                                        ),
                                                        If(
                                                            test=Compare(
                                                                left=Name(id='nb_service_unavailable_codes', ctx=Load()),
                                                                ops=[LtE()],
                                                                comparators=[Constant(value=3, kind=None)],
                                                            ),
                                                            body=[Continue()],
                                                            orelse=[],
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='with_context',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[
                                                                            keyword(
                                                                                arg='automatically_triggered',
                                                                                value=Constant(value=True, kind=None),
                                                                            ),
                                                                        ],
                                                                    ),
                                                                    attr='_trigger_fetch_images_cron',
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
                                                                                attr='now',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Add(),
                                                                        right=Call(
                                                                            func=Name(id='timedelta', ctx=Load()),
                                                                            args=[],
                                                                            keywords=[
                                                                                keyword(
                                                                                    arg='hours',
                                                                                    value=Constant(value=1.0, kind=None),
                                                                                ),
                                                                            ],
                                                                        ),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='warning',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='received too many service_unavailable responses. delegating remaining images to next cron run.', kind=None)],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        Break(),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(id='response', ctx=Load()),
                                                                    attr='status_code',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='requests', ctx=Load()),
                                                                            attr='codes',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='too_many_requests',
                                                                        ctx=Load(),
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
                                                                                args=[],
                                                                                keywords=[
                                                                                    keyword(
                                                                                        arg='automatically_triggered',
                                                                                        value=Constant(value=True, kind=None),
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            attr='_trigger_fetch_images_cron',
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
                                                                                        attr='now',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[],
                                                                                    keywords=[],
                                                                                ),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Name(id='timedelta', ctx=Load()),
                                                                                    args=[],
                                                                                    keywords=[
                                                                                        keyword(
                                                                                            arg='days',
                                                                                            value=Constant(value=1.0, kind=None),
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='warning',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='search quota exceeded. delegating remaining images to next cron run.', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[
                                                                If(
                                                                    test=Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='response', ctx=Load()),
                                                                            attr='status_code',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[Eq()],
                                                                        comparators=[
                                                                            Attribute(
                                                                                value=Attribute(
                                                                                    value=Name(id='requests', ctx=Load()),
                                                                                    attr='codes',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                attr='bad_request',
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
                                                                                        args=[Constant(value='Your API Key or your Search Engine ID is incorrect.', kind=None)],
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
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='RequestConnectionError', ctx=Load()),
                                            name=None,
                                            body=[
                                                AugAssign(
                                                    target=Name(id='nb_timeouts', ctx=Store()),
                                                    op=Add(),
                                                    value=Constant(value=1, kind=None),
                                                ),
                                                If(
                                                    test=Compare(
                                                        left=Name(id='nb_timeouts', ctx=Load()),
                                                        ops=[LtE()],
                                                        comparators=[Constant(value=3, kind=None)],
                                                    ),
                                                    body=[Continue()],
                                                    orelse=[],
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='with_context',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='automatically_triggered',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                            attr='_trigger_fetch_images_cron',
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
                                                                        attr='now',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[],
                                                                    keywords=[],
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Name(id='timedelta', ctx=Load()),
                                                                    args=[],
                                                                    keywords=[
                                                                        keyword(
                                                                            arg='hours',
                                                                            value=Constant(value=1.0, kind=None),
                                                                        ),
                                                                    ],
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='_logger', ctx=Load()),
                                                            attr='warning',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='encountered too many timeouts. delegating remaining images to next cron run.', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ),
                                                Break(),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                                Assign(
                                    targets=[Name(id='response_content', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='response', ctx=Load()),
                                            attr='json',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='int', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Subscript(
                                                        value=Name(id='response_content', ctx=Load()),
                                                        slice=Constant(value='searchInformation', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='totalResults', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='item', ctx=Store()),
                                            iter=Subscript(
                                                value=Name(id='response_content', ctx=Load()),
                                                slice=Constant(value='items', kind=None),
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='image', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='_get_image_from_url',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Subscript(
                                                                        value=Name(id='item', ctx=Load()),
                                                                        slice=Constant(value='link', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Name(id='image', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[
                                                                        Attribute(
                                                                            value=Name(id='product', ctx=Load()),
                                                                            attr='image_1920',
                                                                            ctx=Store(),
                                                                        ),
                                                                    ],
                                                                    value=Name(id='image', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                                Break(),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Tuple(
                                                                elts=[
                                                                    Name(id='RequestConnectionError', ctx=Load()),
                                                                    Name(id='UserError', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            name=None,
                                                            body=[Pass()],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='product', ctx=Load()),
                                            attr='image_fetch_pending',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=False, kind=None),
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
                                            attr='commit',
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
                            value=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='products_to_process', ctx=Load()),
                                            attr='filtered',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='image_1920', kind=None)],
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
                    name='_fetch_image_urls_from_google',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='barcode', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Fetch the first 10 image URLs from the Google Custom Search API.\n\n        :param string barcode: A product's barcode\n        :return: A response or None\n        :rtype: Response\n        ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='barcode', ctx=Load()),
                            ),
                            body=[Return(value=None)],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='ir.config_parameter', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_session',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Constant(value='https://customsearch.googleapis.com/customsearch/v1', kind=None),
                                    ),
                                    keyword(
                                        arg='params',
                                        value=Dict(
                                            keys=[
                                                Constant(value='cx', kind=None),
                                                Constant(value='safe', kind=None),
                                                Constant(value='searchType', kind=None),
                                                Constant(value='key', kind=None),
                                                Constant(value='rights', kind=None),
                                                Constant(value='imgSize', kind=None),
                                                Constant(value='imgType', kind=None),
                                                Constant(value='fields', kind=None),
                                                Constant(value='q', kind=None),
                                            ],
                                            values=[
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='ICP', ctx=Load()),
                                                                attr='get_param',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='google.pse.id', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Constant(value='active', kind=None),
                                                Constant(value='image', kind=None),
                                                Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='ICP', ctx=Load()),
                                                                attr='get_param',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='google.custom_search.key', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        attr='strip',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                Constant(value='cc_publicdomain,cc_attribute,cc_sharealike', kind=None),
                                                Constant(value='large', kind=None),
                                                Constant(value='photo', kind=None),
                                                Constant(value='searchInformation/totalResults,items(link)', kind=None),
                                                Name(id='barcode', ctx=Load()),
                                            ],
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
                    name='_get_image_from_url',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Retrieve an image from the URL.\n\n        If the url contains 'x-raw-image:///', the request failed or the response header\n        'Content-Type' does not contain 'image/', return None\n\n        :param string url: url of an image\n        :return: The retrieved image or None\n        :rtype: bytes\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='image', ctx=Store())],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='x-raw-image:///', kind=None),
                                ops=[NotIn()],
                                comparators=[Name(id='url', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='response', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_session',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Constant(value=5, kind=None),
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
                                                left=Attribute(
                                                    value=Name(id='response', ctx=Load()),
                                                    attr='status_code',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='requests', ctx=Load()),
                                                            attr='codes',
                                                            ctx=Load(),
                                                        ),
                                                        attr='ok',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Compare(
                                                left=Constant(value='image/', kind=None),
                                                ops=[In()],
                                                comparators=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='headers',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='Content-Type', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='image', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='base64', ctx=Load()),
                                                    attr='b64encode',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='response', ctx=Load()),
                                                        attr='content',
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
                        Return(
                            value=Name(id='image', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_trigger_fetch_images_cron',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='at', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Create a trigger for the con `ir_cron_fetch_image`.\n\n        By default the cron is scheduled to be executed as soon as possible but\n        the optional `at` argument may be given to delay the execution later\n        with a precision down to 1 minute.\n\n        :param Optional[datetime.datetime] at:\n            When to execute the cron, at one moments in time instead of as soon as possible.\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
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
                                        args=[Constant(value='product_images.ir_cron_fetch_image', kind=None)],
                                        keywords=[],
                                    ),
                                    attr='_trigger',
                                    ctx=Load(),
                                ),
                                args=[Name(id='at', ctx=Load())],
                                keywords=[],
                            ),
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
                                    attr='commit',
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
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
