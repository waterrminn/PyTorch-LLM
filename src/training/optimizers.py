from torch.optim import AdamW



def get_optimizer_params(model, #, #, weight_decay=0.0):
    """
    Optimizer parameters by encoder and decoder
    """
    param_optimizer = list(#)
    no_decay = ["bias", "LayerNorm.bias", "LayerNorm.weight"]
    optimizer_parameters = [
        {'params': [p for n, p in # if not any(nd in n for nd in no_decay)],
        'lr': #, 'weight_decay': #},
        {'params': [p for n, p in # if any(nd in n for nd in no_decay)],
        'lr': #, 'weight_decay': #},
        {'params': [p for n, p in # if "model" not in n],
        'lr': #, 'weight_decay': #}
    ]
    return optimizer_parameters


def get_optimizer(cfg, model):
    """ Select the optimizer """
    if cfg.name == #:
        opt = #(filter(lambda p: p.requires_grad, model.parameters()),
                    lr=#,
                    )
    else:
        print('Optimizer needs to be included in code')
    return opt
